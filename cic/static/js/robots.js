
import { getData } from "./request.js";

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
    this.showResponse("starting")
    getData("/robots/start", this.showResponse);
  }
  
  handleStopClick(event) {
    event.preventDefault();
    this.showResponse("stopping")
    getData("/robots/stop", this.showResponse);
  }

  showResponse(data) {
    const robotsCard = document.querySelector(".robots-card");
    let code = robotsCard.querySelector("code");
    code.innerText = data;
  }
}

