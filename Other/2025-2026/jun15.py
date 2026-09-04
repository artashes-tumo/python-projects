


def interview_qualified(very_easy1, very_easy2, easy1, easy2, medium1, medium2, hard1, hard2, time):

    interview_qualifications = {
        "difficulty": [0, 0, 0, 0, 0, 0, 0, 0],
        "duration": 0
    }


    interview_qualifications["duration"] = time
    interview_qualifications["difficulty"][0] = very_easy1
    interview_qualifications["difficulty"][1] = very_easy2
    interview_qualifications["difficulty"][2] = easy1
    interview_qualifications["difficulty"][3] = easy2
    interview_qualifications["difficulty"][4] = medium1
    interview_qualifications["difficulty"][5] = medium2
    interview_qualifications["difficulty"][6] = hard1
    interview_qualifications["difficulty"][7] = hard2

    if interview_qualifications["duration"] > 120:
        print("The interview was too long. You may want to work on time management.")
        return "disqualified"

    elif interview_qualifications["difficulty"][0] > 5:
        print("You spent too much time on very easy questions. Try to be more efficient.")
        return "disqualified"

    elif interview_qualifications["difficulty"][1] > 10:
        print("You spent too much time on easy questions. Try to be more efficient.")
        return "disqualified"

    elif interview_qualifications["difficulty"][2] > 15:
        print("You spent too much time on medium questions. Try to be more efficient.")
        return "disqualified"

    elif interview_qualifications["difficulty"][3] > 20:
        print("You spent too much time on the first hard question. Try to be more efficient.")
        return "disqualified"

    elif interview_qualifications["difficulty"][4] > 20:
        print("You spent too much time on the second hard question. Try to be more efficient.")
        return "disqualified"
    
    elif any(minutes == 0 for minutes in interview_qualifications["difficulty"]):
        print("You did not answer one or more questions. Please try to answer every question.")
        return "disqualified"

    else:
        print("Congratulations! You are qualified for the next round of interviews.")
        return "qualified"

interview_qualified(5, 5, 10, 10, 15, 15, 20, 20, 120)