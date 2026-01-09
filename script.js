<script>
const OBR = window.OBR;

let currentTokenId = null;

OBR.onReady(async () => {
    document.getElementById('status-bar').innerText = "SELEZIONA UNA PEDINA";
    document.getElementById('status-bar').style.background = "#bc6c4d";

    setInterval(async () => {
        const selection = await OBR.player.getSelection();
        if (!selection || selection.length === 0) return;

        if (selection[0] !== currentTokenId) {
            currentTokenId = selection[0];

            const items = await OBR.scene.items.getItems([currentTokenId]);
            if (!items.length) return;

            const token = items[0];

            // ORA CHI SELEZIONA PUÒ MODIFICARE
            document.getElementById('status-bar').innerText =
                "✏️ MODIFICANDO: " + token.name;
            document.getElementById('status-bar').style.background = "#3e5437";

            // abilita tutti i campi
            document.querySelectorAll('.save-field').forEach(el => {
                el.disabled = false;
            });

            // carica dati salvati
            const d = token.metadata["fabula-data"] || {};

            const fields = [
                "char_name",
                "forza","destrezza","mente","volonta",
                "pv","mp","pi",
                "classi","abilita"
            ];

            fields.forEach(id => {
                document.getElementById(id).value = d[id] || "";
            });
        }
    }, 600);
});

async function saveData() {
    if (!currentTokenId) return;

    const data = {};
    document.querySelectorAll('.save-field').forEach(el => {
        data[el.id] = el.value;
    });

    await OBR.scene.items.updateItems([currentTokenId], items => {
        for (let item of items) {
            item.metadata["fabula-data"] = data;
        }
    });
}

// salva automaticamente mentre scrivi
document.querySelectorAll('.save-field').forEach(el => {
    el.addEventListener('input', saveData);
});
</script>
