package com.example.spa_and_api_android

import android.content.Intent
import android.os.Bundle
import android.view.View
import android.view.View.GONE
import android.view.View.VISIBLE
import android.widget.Button
import android.widget.ImageButton
import android.widget.LinearLayout
import androidx.appcompat.app.AppCompatActivity
import androidx.lifecycle.lifecycleScope
import kotlinx.coroutines.launch
import org.json.JSONObject

open class BaseActivity: AppCompatActivity() {

    fun changeVisibility(view: View, visibility: Int? = null) {
        if (visibility == null) {
            if (view.visibility == GONE) {
                view.visibility = VISIBLE
            } else {
                view.visibility = GONE
            }
        }
        else {
            view.visibility = visibility
        }
    }

    fun <T> startNewActivity(target: Class<T>, extras: Bundle? = null) {
        val intent = Intent(this, target)
        intent.flags = Intent.FLAG_ACTIVITY_NEW_TASK or Intent.FLAG_ACTIVITY_CLEAR_TASK
        extras?.let { intent.putExtras(it) }
        startActivity(intent)
    }

    fun setUpViewBase(view: Int) {
        setContentView(view)
        val navBarCollapse: LinearLayout = findViewById(R.id.nav_bar_collapse)
        val navBarToggle: ImageButton = findViewById(R.id.nav_bar_toggle)
        navBarToggle.setOnClickListener {
            changeVisibility(navBarCollapse)
        }
        val navBarLogo: ImageButton = findViewById(R.id.nav_bar_logo)
        val navBarTitle: Button = findViewById(R.id.nav_bar_title)
        navBarLogo.setOnClickListener {
            startNewActivity(IndexActivity::class.java)
        }
        navBarTitle.setOnClickListener {
            startNewActivity(IndexActivity::class.java)
        }
    }

    fun setNavBarBeforeLogin() {
        val navBarLink1: Button = findViewById(R.id.nav_bar_link1)
        val navBarLink2: Button = findViewById(R.id.nav_bar_link2)
        navBarLink1.setOnClickListener {
            startNewActivity(UserAuthActivity::class.java)
        }
        navBarLink2.setOnClickListener {
            startNewActivity(UserNewActivity::class.java)
        }
    }

    fun setNavBarAfterLogin() {
        val navBarLink1: Button = findViewById(R.id.nav_bar_link1)
        val navBarLink2: Button = findViewById(R.id.nav_bar_link2)
        lifecycleScope.launch {
            val (status: Int, json: JSONObject?) = ApiClient.accessUserGet()
            if (status == 200) {
                navBarLink1.text = "${json?.getString("name")} 様"
                navBarLink2.text = "ログアウト"
                navBarLink1.setOnClickListener {
                    startNewActivity(UserInfoActivity::class.java)
                }
                navBarLink2.setOnClickListener {
                    JwtManager.clearJwt()
                    startNewActivity(IndexActivity::class.java)
                }
            } else {
                if (this@BaseActivity::class.java == IndexActivity::class.java) {
                    navBarLink1.setOnClickListener {
                        startNewActivity(UserAuthActivity::class.java)
                    }
                    navBarLink2.setOnClickListener {
                        startNewActivity(UserNewActivity::class.java)
                    }
                }
                else {
                    startNewActivity(UserAuthActivity::class.java)
                }
            }
        }
    }

    fun setSubmitButtonOnClickListener(function: () -> Unit) {
        val submitButton: Button = findViewById(R.id.submit_button)
        submitButton.setOnClickListener {
            function()
        }
    }

}
