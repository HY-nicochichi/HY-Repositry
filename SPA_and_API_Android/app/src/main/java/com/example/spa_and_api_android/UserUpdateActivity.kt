package com.example.spa_and_api_android

import android.os.Bundle
import android.view.View.VISIBLE
import android.widget.EditText
import android.widget.TextView
import androidx.lifecycle.lifecycleScope
import kotlinx.coroutines.launch
import org.json.JSONObject

class UserUpdateActivity: BaseActivity()  {

    private fun getParam(): String {
        var param: String? = intent.getStringExtra("param")
        if (param == null) {
            param = "メールアドレス"
        }
        return param
    }

    private fun setHintsAndInputType(hints: List<String>, inputType: Int, fields: List<EditText>) {
        fields.forEachIndexed { index, editText ->
            editText.hint = hints[index]
            editText.inputType = inputType
            if (inputType == android.text.InputType.TYPE_TEXT_VARIATION_PASSWORD) {
                editText.transformationMethod = android.text.method.PasswordTransformationMethod.getInstance()
            }
        }
    }

    private fun setUpdatePage() {
        val updatePageTitle: TextView = findViewById(R.id.update_page_title)
        val currentVal: EditText = findViewById(R.id.current_val)
        val newVal: EditText = findViewById(R.id.new_val)
        val checkVal: EditText = findViewById(R.id.check_val)
        val param: String = getParam()
        when (param) {
            "パスワード" -> {
                updatePageTitle.text = "パスワードの変更"
                setHintsAndInputType(
                    listOf("現パスワード", "新パスワード", "新パスワード(確認)"),
                    android.text.InputType.TYPE_TEXT_VARIATION_PASSWORD,
                    listOf(currentVal, newVal, checkVal)
                )
            }
            "ユーザーネーム" -> {
                updatePageTitle.text = "ユーザーネームの変更"
                setHintsAndInputType(
                    listOf("現ユーザーネーム", "新ユーザーネーム", "新ユーザーネーム(確認)"),
                    android.text.InputType.TYPE_TEXT_VARIATION_PERSON_NAME,
                    listOf(currentVal, newVal, checkVal)
                )
            }
        }
    }

    private fun tryUpdateUser() {
        val param: String = getParam()
        val alertBox: TextView = findViewById(R.id.alert_box)
        val currentVal: EditText = findViewById(R.id.current_val)
        val newVal: EditText = findViewById(R.id.new_val)
        val checkVal: EditText = findViewById(R.id.check_val)
        val currentValString: String = currentVal.text.toString()
        val newValString: String = newVal.text.toString()
        val checkValString: String = checkVal.text.toString()
        if (currentValString == "" || newValString == "" || checkValString == "") {
            alertBox.text = "※ 未入力の項目がありました"
        }
        else {
            lifecycleScope.launch {
                val (status: Int, json: JSONObject?) = ApiClient.accessUserPut(
                    param, currentValString, newValString, checkValString
                )
                if (status == 200) {
                    startNewActivity(UserInfoActivity::class.java)
                }
                else {
                    alertBox.text = "※ ${json?.getString("msg")}"
                }
            }
        }
        changeVisibility(alertBox, VISIBLE)
        currentVal.setText("")
        newVal.setText("")
        checkVal.setText("")
    }

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setUpViewBase(R.layout.activity_user_update)
        setNavBarAfterLogin()
        setUpdatePage()
        setSubmitButtonOnClickListener(::tryUpdateUser)
    }

}
