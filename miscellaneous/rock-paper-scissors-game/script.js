function getRandomComputerResult() {
    const options = ['Rock', 'Paper', 'Scissors'];
    const randomIndex = Math.floor(Math.random() * options.length);
    return options[randomIndex];
}

let playerScore = 0;
let computerScore = 0;

function hasPlayerWonTheRound(player, computer) {
/*     if (player === 'Rock' && computer === 'Scissors') {
        return true;
    } else if (player ==='Scissors' && computer === 'Paper') {
        return true;
    } else if (player ==='Paper' && computer === 'Rock') {
        return true;
    } else if (player === computer) {
        return false;
    } else {
        return false;
    } */
   return (
    (player === 'Rock' && computer === 'Scissors') ||
    (player === 'Scissors' && computer === 'Paper') ||
    (player === 'Paper' && computer === 'Rock')
   );
}

function getRoundResults(userOption) {
    const computerResult = getRandomComputerResult();
    
}