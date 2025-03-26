package com.example.spa_and_api_android

import android.os.Bundle
import android.widget.Button
import android.widget.TextView
import androidx.lifecycle.lifecycleScope
import kotlinx.coroutines.launch
import org.json.JSONObject

class UserInfoActivity: BaseActivity() {

    private fun tryDeleteUser() {
        lifecycleScope.launch {
            val (status: Int, json: JSONObject?) = ApiClient.accessUserDelete()
            if (status == 200) {
                JwtManager.clearJwt()
                startNewActivity(IndexActivity::class.java)
            }
        }
    }

    private fun setUserInfoPage() {
        val userName: TextView = findViewById(R.id.user_name)
        val mailAddress: TextView = findViewById(R.id.mail_address)
        lifecycleScope.launch {
            val (status: Int, json: JSONObject?) = ApiClient.accessUserGet()
            if (status == 200) {
                userName.text = "ユーザーネーム：${json?.getString("name")}"
                mailAddress.text = "メールアドレス：${json?.getString("mail")}"
            }
        }
        val buttonUpdateName: Button = findViewById(R.id.button_update_name)
        buttonUpdateName.setOnClickListener {
            startNewActivity(
                UserUpdateActivity::class.java,
                Bundle().apply{putString("param", "ユーザーネーム")}
            )
        }
        val buttonUpdateMail: Button = findViewById(R.id.button_update_mail)
        buttonUpdateMail.setOnClickListener {
            startNewActivity(
                UserUpdateActivity::class.java,
                Bundle().apply{putString("param", "メールアドレス")}
            )
        }
        val buttonUpdatePassword: Button = findViewById(R.id.button_update_password)
        buttonUpdatePassword.setOnClickListener {
            startNewActivity(
                UserUpdateActivity::class.java,
                Bundle().apply{putString("param", "パスワード")}
            )
        }
        val buttonUserDelete: Button = findViewById(R.id.button_user_delete)
        buttonUserDelete.setOnClickListener {
            tryDeleteUser()
        }
    }

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setUpViewBase(R.layout.activity_user_info)
        setNavBarAfterLogin()
        setUserInfoPage()
    }

}
