package com.example.spa_and_api_android

import kotlinx.coroutines.Dispatchers
import kotlinx.coroutines.withContext
import okhttp3.MediaType.Companion.toMediaType
import okhttp3.OkHttpClient
import okhttp3.Request
import okhttp3.RequestBody.Companion.toRequestBody
import org.json.JSONObject

object ApiClient {

    private lateinit var client: OkHttpClient
    private lateinit var JWT_API_ROUTE: String
    private lateinit var USER_API_ROUTE: String

    fun init() {
        client = OkHttpClient()
        JWT_API_ROUTE = "http://10.0.2.2:5000/jwt/"
        USER_API_ROUTE = "http://10.0.2.2:5000/user/"
    }

    suspend fun accessJwtPost(
        mail: String, password: String
    ): Pair<Int, JSONObject?>
    = withContext(Dispatchers.IO) {
        val requestBody = JSONObject(
            mapOf(
                "mail" to mail,
                "password" to password
            )
        ).toString()
        val request = Request.Builder()
            .url(JWT_API_ROUTE)
            .post(requestBody.toRequestBody("application/json".toMediaType()))
            .build()
        client.newCall(request).execute().use { response ->
            val status: Int = response.code
            val json: JSONObject? = response.body?.string()?.let { JSONObject(it) }
            return@withContext Pair(status, json)
        }
    }

    suspend fun accessUserGet(): Pair<Int, JSONObject?>
    = withContext(Dispatchers.IO) {
        val request = Request.Builder()
            .url(USER_API_ROUTE)
            .addHeader("Authorization", "Bearer ${JwtManager.getJwt()}")
            .get()
            .build()
        client.newCall(request).execute().use { response ->
            val status: Int = response.code
            val json: JSONObject? = response.body?.string()?.let { JSONObject(it) }
            return@withContext Pair(status, json)
        }
    }

    suspend fun accessUserPost(
        mail: String, password: String, name: String
    ): Pair<Int, JSONObject?>
    = withContext(Dispatchers.IO) {
        val requestBody = JSONObject(
            mapOf(
                "mail" to mail,
                "password" to password,
                "name" to name
            )
        ).toString()
        val request = Request.Builder()
            .url(USER_API_ROUTE)
            .post(requestBody.toRequestBody("application/json".toMediaType()))
            .build()
        client.newCall(request).execute().use { response ->
            val status: Int = response.code
            val json: JSONObject? = response.body?.string()?.let { JSONObject(it) }
            return@withContext Pair(status, json)
        }
    }

    suspend fun accessUserPut(
        param: String, currentVal: String, newVal: String, checkVal: String
    ): Pair<Int, JSONObject?>
    = withContext(Dispatchers.IO) {
        val requestBody = JSONObject(
            mapOf(
                "param" to param,
                "current_val" to currentVal,
                "new_val" to newVal,
                "check_val" to checkVal
            )
        ).toString()
        val request = Request.Builder()
            .url(USER_API_ROUTE)
            .put(requestBody.toRequestBody("application/json".toMediaType()))
            .addHeader("Authorization", "Bearer ${JwtManager.getJwt()}")
            .build()
        client.newCall(request).execute().use { response ->
            val status: Int = response.code
            val json: JSONObject? = response.body?.string()?.let { JSONObject(it) }
            return@withContext Pair(status, json)
        }
    }

    suspend fun accessUserDelete(): Pair<Int, JSONObject?>
    = withContext(Dispatchers.IO) {
        val request = Request.Builder()
            .url(USER_API_ROUTE)
            .addHeader("Authorization", "Bearer ${JwtManager.getJwt()}")
            .delete()
            .build()
        client.newCall(request).execute().use { response ->
            val status: Int = response.code
            val json: JSONObject? = response.body?.string()?.let { JSONObject(it) }
            return@withContext Pair(status, json)
        }
    }
}
