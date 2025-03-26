package com.example.spa_and_api_android

import android.os.Bundle
import android.view.View.VISIBLE
import android.widget.EditText
import android.widget.TextView
import androidx.lifecycle.lifecycleScope
import kotlinx.coroutines.launch
import org.json.JSONObject

class UserNewActivity: BaseActivity()  {

    private fun tryCreateUser() {
        val alertBox: TextView = findViewById(R.id.alert_box)
        val inputMail: EditText = findViewById(R.id.input_mail)
        val inputPassword: EditText = findViewById(R.id.input_password)
        val inputName: EditText = findViewById(R.id.input_name)
        val inputMailString: String = inputMail.text.toString()
        val inputPasswordString: String = inputPassword.text.toString()
        val inputNameString: String = inputName.text.toString()
        if (inputMailString == "" || inputPasswordString == "" || inputNameString == "") {
            alertBox.text = "※ 未入力の項目がありました"
        }
        else {
            lifecycleScope.launch {
                val (status1: Int, json1: JSONObject?) = ApiClient.accessUserPost(
                    inputMailString, inputPasswordString, inputNameString
                )
                if (status1 == 200) {
                    val (status2: Int, json2: JSONObject?) = ApiClient.accessJwtPost(
                        inputMailString, inputPasswordString
                    )
                    val accessToken = json2?.getString("access_token")
                    if (accessToken != null) {
                        JwtManager.saveJwt(accessToken)
                    }
                    startNewActivity(IndexActivity::class.java)
                }
                else {
                    alertBox.text = "※ ${json1?.getString("msg")}"
                }
            }
        }
        changeVisibility(alertBox, VISIBLE)
        inputMail.setText("")
        inputPassword.setText("")
        inputName.setText("")
    }

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setUpViewBase(R.layout.activity_user_new)
        setNavBarBeforeLogin()
        setSubmitButtonOnClickListener(::tryCreateUser)
    }

}
