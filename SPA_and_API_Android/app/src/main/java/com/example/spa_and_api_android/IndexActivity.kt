package com.example.spa_and_api_android

import android.os.Bundle

class IndexActivity: BaseActivity() {

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setUpViewBase(R.layout.activity_index)
        setNavBarAfterLogin()
    }

}
