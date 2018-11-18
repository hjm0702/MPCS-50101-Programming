'''

1. For each algorithm, what is the factor that can affect the number of questions asked (the “problem size”)?

    Algorithm 1 - Any factor can affect the number of questions asked.
    However, if a room is too huge for people to hear your name or questions clearly,
    you may have to ask the questions a few times more.

    Algorithm 2 - The total number of people in the room and your luck affect the number of questions asked.
    Since you have to ask question one on one, you have to ask the same question as many times as the number of people.
    However, if you are lucky enough and meet someone with the same name as you, you can quit the process earlier than expected.


    Algorithm 3 - Same as the 2nd answer, the total number of people in the room and your luck affect the number of questions asked.
    Since you cannot find the answer directly but through a series of questions by others,
    if the number of people increases, the number of questions asked also increases.
    However, if you are lucky enough so you or other person meets someone with the same name as you early,
    you can quit the process earlier than expected.

2. In the worst case, how many questions will be asked for each of the three algorithms?

    Algorithm 1 - 1

    Algorithm 2 - n

    Algorithm 3 - n^2-n+1
        If you have one person, you should ask 1 question.
        If you have two, 3 questions,
        If you have three, 7 questions.
        ...


3. For each algorithm, say whether it is constant, linear, or quadratic in the problem size in the worst case.

    Algorithm 1 - constant

    Algorithm 2 - linear

    Algorithm 3 - quadratic 
'''
