
export class RobotsForm {
  constructor() {
    this.robotsCard = document.querySelector(".robots-card");
    this.form = this.robotsCard.querySelector(".robots-form");
    this.startButton = this.form.querySelector("button[data-action='start']");
    this.startButton.addEventListener("click", this.handleStartClick.bind(this));
    this.stopButton = this.form.querySelector("button[data-action='stop']");
    this.stopButton.addEventListener("click", this.handleStopClick.bind(this));
  }

  handleStartClick(event) {
    event.preventDefault();
    let code = this.robotsCard.querySelector("code");
    code.innerText = "started";
  }
  
  handleStopClick(event) {
    event.preventDefault();
    let code = this.robotsCard.querySelector("code");
    code.innerText = "stopped";
  }

  showResponse(data) {
    const robotsCard = document.querySelector(".robots-card");
    let code = robotsCard.querySelector("code");
    code.innerText = data;
  }
}

