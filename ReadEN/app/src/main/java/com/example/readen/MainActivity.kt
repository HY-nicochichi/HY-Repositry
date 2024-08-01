package com.example.readen

import androidx.appcompat.app.AppCompatActivity
import android.os.Bundle
import android.widget.Button
import android.content.Intent

class MainActivity : AppCompatActivity() {
    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.activity_main)

        val button1 = findViewById<Button>(R.id.ButtonQ1)
        button1.setOnClickListener {
            val intentQuiz = Intent(this, QuizActivity::class.java)
            val quizNo = 1
            intentQuiz.putExtra("quizNo", quizNo)
            startActivity(intentQuiz)
        }

        val button2 = findViewById<Button>(R.id.ButtonQ2)
        button2.setOnClickListener {
            val intentQuiz = Intent(this, QuizActivity::class.java)
            val quizNo = 2
            intentQuiz.putExtra("quizNo", quizNo)
            startActivity(intentQuiz)
        }

        val button3 = findViewById<Button>(R.id.ButtonQ3)
        button3.setOnClickListener {
            val intentQuiz = Intent(this, QuizActivity::class.java)
            val quizNo = 3
            intentQuiz.putExtra("quizNo", quizNo)
            startActivity(intentQuiz)
        }
    }
}
