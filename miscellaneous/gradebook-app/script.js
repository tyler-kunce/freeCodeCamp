function getAverage(scores) {
    let numerator = 0;
    let denominator = 0;
    for (let i = 0; i < scores.length; i++) {
        numerator += scores[i];
        denominator = scores.length;
    }
    return numerator / denominator;
}

function getGrade(score) {
    if (score === 100) {
        return "A++";
    } else if (score <= 99 && score >= 90) {
        return "A";
    } else if (score <= 89 && score >= 80) {
        return "B";
    } else if (score <= 79 && score >= 70) {
        return "C";
    } else if (score <= 69 && score >= 60) {
        return "D";
    } else {
        return "F";
    }
}

function hasPassingGrade(score) {
    if (getGrade(score) !== "F") {
        return true;
    } else {
        return false;
    }
}

function studentMsg(totalScores, studentScore) {
    let classAverage = getAverage(totalScores);
    let studentGrade = getGrade(studentScore);
    if (studentGrade === "F") {
        return "Class average: " + classAverage + ". Your grade: " + studentGrade + ". You failed the course.";
    } else {
        return "Class average: " + classAverage + ". Your grade: " + studentGrade + ". You passed the course.";
    }
}