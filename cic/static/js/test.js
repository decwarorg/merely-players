
import { getData } from "./request.js";

export class TestForm {
  constructor() {
    this.testCard = document.querySelector(".test-card");
    this.form = this.testCard.querySelector(".test-form");
    this.clearButton = this.form.querySelector("button[data-action='clear']");
    this.clearButton.addEventListener(
      "click",
      this.handleClearClick.bind(this)
    );
    this.sendButton = this.form.querySelector("button[data-action='read']");
    this.sendButton.addEventListener("click", this.handleSendClick.bind(this));
  }

  handleClearClick(event) {
    event.preventDefault();
    let code = this.testCard.querySelector("code");
    code.innerText = "";
  }

  handleSendClick(event) {
    event.preventDefault();
    const input = document.querySelector(".test-card input");
    const endpoint = input.value;
    getData(endpoint, this.showResponse);
  }

  showResponse(data) {
    const testCard = document.querySelector(".test-card");
    let code = testCard.querySelector("code");
    code.innerText = data;
  }
}

