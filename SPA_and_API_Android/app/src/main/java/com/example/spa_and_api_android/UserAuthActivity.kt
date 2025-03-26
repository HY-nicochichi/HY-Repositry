package com.example.spa_and_api_android

import android.os.Bundle
import android.view.View.VISIBLE
import android.widget.EditText
import android.widget.TextView
import androidx.lifecycle.lifecycleScope
import kotlinx.coroutines.launch
import org.json.JSONObject

class UserAuthActivity: BaseActivity() {

    private fun tryLogin() {
        val alertBox: TextView = findViewById(R.id.alert_box)
        val inputMail: EditText = findViewById(R.id.input_mail)
        val inputPassword: EditText = findViewById(R.id.input_password)
        val inputMailString: String = inputMail.text.toString()
        val inputPasswordString: String = inputPassword.text.toString()
        if (inputMailString == "" || inputPasswordString == "") {
            alertBox.text = "※ 未入力の項目がありました"
        }
        else {
            lifecycleScope.launch {
                val (status: Int, json: JSONObject?) = ApiClient.accessJwtPost(
                    inputMailString, inputPasswordString
                )
                if (status == 200) {
                    val accessToken = json?.getString("access_token")
                    if (accessToken != null) {
                        JwtManager.saveJwt(accessToken)
                    }
                    startNewActivity(IndexActivity::class.java)
                }
                else {
                    alertBox.text = "※ ${json?.getString("msg")}"
                }
            }
        }
        changeVisibility(alertBox, VISIBLE)
        inputMail.setText("")
        inputPassword.setText("")
    }

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setUpViewBase(R.layout.activity_user_auth)
        setNavBarBeforeLogin()
        setSubmitButtonOnClickListener(::tryLogin)
    }

}
