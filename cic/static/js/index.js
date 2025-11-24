
import { GalaxyForm } from "./galaxy.js";
import { RobotsForm } from "./robots.js";

function main() {

  if (document.querySelector(".galaxy-card")) {
    const galaxy = new GalaxyForm();
    galaxy.showResponse("");
  }

  if (document.querySelector(".robots-card")) {
    const robots = new RobotsForm();
    robots.showResponse("");
  }

}

main();
