
import { TestForm } from "./test.js";

function main() {

  if (document.querySelector(".test-card")) {
    const test = new TestForm();
    test.showResponse("");
  }

}

main();
