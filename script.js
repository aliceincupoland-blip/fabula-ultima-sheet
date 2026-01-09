import { room, storage } from "@owlbear-rodeo/sdk";

let playerId = null;

// aspettiamo che Owlbear sia pronto
room.onReady(async () => {
  playerId = room.playerId;
  loadSheet();
});

// raccoglie i dati dalla scheda
function collectData() {
  return {
    name: document.getElementById("name").value,
    job: document.getElementById("job").value,
    level: document.getElementById("level").value,
    might: document.getElementById("might").value,
    dex: document.getElementById("dex").value,
    insight: document.getElementById("insight").value,
    will: document.getElementById("will").value
  };
}

// riempie la scheda
function applyData(data) {
  if (!data) return;
  document.getElementById("name").value = data.name || "";
  document.getElementById("job").value = data.job || "";
  document.getElementById("level").value = data.level || "";
  document.getElementById("might").value = data.might || "";
  document.getElementById("dex").value = data.dex || "";
  document.getElementById("insight").value = data.insight || "";
  document.getElementById("will").value = data.will || "";
}

// salva
async function saveSheet() {
  const data = collectData();
  await storage.setItem(`fabula_${playerId}`, data);
}

// carica
async function loadSheet() {
  const data = await storage.getItem(`fabula_${playerId}`);
  applyData(data);
}

// autosave
document.addEventListener("input", saveSheet);
