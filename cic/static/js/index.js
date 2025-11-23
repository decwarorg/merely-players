
import { GalaxyForm } from "./galaxy.js";

function main() {

  if (document.querySelector(".galaxy-card")) {
    const galaxy = new GalaxyForm();
    galaxy.showResponse("");
  }

}

main();
