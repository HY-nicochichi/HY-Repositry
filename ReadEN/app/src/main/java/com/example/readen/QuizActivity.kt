package com.example.readen

import androidx.appcompat.app.AppCompatActivity
import android.os.Bundle
import android.widget.ImageButton
import android.content.Intent
import android.widget.TextView
import android.widget.Button

class QuizActivity : AppCompatActivity() {
    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.activity_quiz)

        val homeButton = findViewById<ImageButton>(R.id.HomeButton)
        homeButton.setOnClickListener {
            val intentHome = Intent(this, MainActivity::class.java)
            startActivity(intentHome)
        }

        val quizList = arrayOf(
            "My brother lives in Kyoto because he seriously loves temples and shrines.",
            "People will probably elect him the next president of this nation.",
            "Alice bought a video game software for her son yesterday."
        )
        val quizNo = intent.getIntExtra("quizNo", 1)
        val quizNoText = findViewById<TextView>(R.id.QuizNo)
        quizNoText.text = "Q.${quizNo}"
        val quizText = findViewById<TextView>(R.id.QuizText)
        quizText.text = quizList[quizNo-1]

        val buttonOp1 = findViewById<Button>(R.id.ButtonOp1)
        buttonOp1.setOnClickListener {
            val intentAnswer = Intent(this, AnswerActivity::class.java)
            intentAnswer.putExtra("quizNo", quizNo)
            val optionNo = 1
            intentAnswer.putExtra("optionNo", optionNo)
            startActivity(intentAnswer)
        }

        val buttonOp2 = findViewById<Button>(R.id.ButtonOp2)
        buttonOp2.setOnClickListener {
            val intentAnswer = Intent(this, AnswerActivity::class.java)
            intentAnswer.putExtra("quizNo", quizNo)
            val optionNo = 2
            intentAnswer.putExtra("optionNo", optionNo)
            startActivity(intentAnswer)
        }

        val buttonOp3 = findViewById<Button>(R.id.ButtonOp3)
        buttonOp3.setOnClickListener {
            val intentAnswer = Intent(this, AnswerActivity::class.java)
            intentAnswer.putExtra("quizNo", quizNo)
            val optionNo = 3
            intentAnswer.putExtra("optionNo", optionNo)
            startActivity(intentAnswer)
        }

        val buttonOp4 = findViewById<Button>(R.id.ButtonOp4)
        buttonOp4.setOnClickListener {
            val intentAnswer = Intent(this, AnswerActivity::class.java)
            intentAnswer.putExtra("quizNo", quizNo)
            val optionNo = 4
            intentAnswer.putExtra("optionNo", optionNo)
            startActivity(intentAnswer)
        }

        val buttonOp5 = findViewById<Button>(R.id.ButtonOp5)
        buttonOp5.setOnClickListener {
            val intentAnswer = Intent(this, AnswerActivity::class.java)
            intentAnswer.putExtra("quizNo", quizNo)
            val optionNo = 5
            intentAnswer.putExtra("optionNo", optionNo)
            startActivity(intentAnswer)
        }
    }
}
