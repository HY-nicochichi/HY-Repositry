package com.example.spa_and_api_android

import android.app.Application

class TheApp : Application() {

    override fun onCreate() {
        super.onCreate()
        JwtManager.init(this)
        ApiClient.init()
    }

}
