package com.example.spa_and_api_android

import android.content.Context
import android.content.SharedPreferences
import androidx.security.crypto.EncryptedSharedPreferences
import androidx.security.crypto.MasterKey

object JwtManager {

    private lateinit var sharedPreferences: SharedPreferences

    fun init(context: Context) {
        val masterKey = MasterKey.Builder(context)
            .setKeyScheme(MasterKey.KeyScheme.AES256_GCM)
            .build()
        sharedPreferences = EncryptedSharedPreferences.create(
            context,
            "secure_prefs",
            masterKey,
            EncryptedSharedPreferences.PrefKeyEncryptionScheme.AES256_SIV,
            EncryptedSharedPreferences.PrefValueEncryptionScheme.AES256_GCM
        )
    }

    fun saveJwt(token: String) {
        sharedPreferences.edit().apply {
            putString("jwt", token)
            apply()
        }
    }

    fun getJwt(): String? {
        return sharedPreferences.getString("jwt", null)
    }

    fun clearJwt() {
        sharedPreferences.edit().apply {
            remove("jwt")
            apply()
        }
    }

}
