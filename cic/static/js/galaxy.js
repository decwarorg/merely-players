
import { getData } from "./request.js";

export class GalaxyForm {
  constructor() {
    this.galaxyCard = document.querySelector(".galaxy-card");
    this.form = this.galaxyCard.querySelector(".galaxy-form");
    this.clearButton = this.form.querySelector("button[data-action='clear']");
    this.clearButton.addEventListener("click", this.handleClearClick.bind(this));
    this.sendButton = this.form.querySelector("button[data-action='read']");
    this.sendButton.addEventListener("click", this.handleSendClick.bind(this));
  }

  handleClearClick(event) {
    event.preventDefault();
    let code = this.galaxyCard.querySelector("code");
    code.innerText = "";
  }

  handleSendClick(event) {
    event.preventDefault();
    const input = document.querySelector(".galaxy-card input");
    const endpoint = input.value;
    getData(endpoint, this.showResponse);
  }

  showResponse(data) {
    const galaxyCard = document.querySelector(".galaxy-card");
    let code = galaxyCard.querySelector("code");
    code.innerText = data;
  }
}

