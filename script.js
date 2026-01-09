<script>

    alert("SCRIPT CARICATO");

const OBR = window.OBR;

let currentTokenId = null;

// abilita subito i campi (IMPORTANTISSIMO)
function enableFields(enabled = true) {
    document.querySelectorAll('.save-field').forEach(el => {
        el.disabled = !enabled;
    });
}

enableFields(true); // <-- FIX CHIAVE

OBR.onReady(() => {
    const status = document.getElementById('status-bar');
    status.innerText = "ADD-ON PRONTO – SELEZIONA UNA PEDINA";
    status.style.background = "#3e5437";

    setInterval(async () => {
        const selection = await OBR.player.getSelection();

        if (!selection || selection.length === 0) {
            status.innerText = "NESSUNA PEDINA SELEZIONATA";
            status.style.background = "#bc6c4d";
            currentTokenId = null;
            return;
        }

        if (selection[0] !== currentTokenId) {
            currentTokenId = selection[0];

            const items = await OBR.scene.items.getItems([currentTokenId]);
            if (!items.length) return;

            const token = items[0];

            status.innerText = "✏️ MODIFICANDO: " + (token.name || "Pedina");
            status.style.background = "#3e5437";

            // carica dati
            const d = token.metadata["fabula-data"] || {};

            document.querySelectorAll('.save-field').forEach(el => {
                el.value = d[el.id] || "";
            });
        }
    }, 500);
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

document.querySelectorAll('.save-field').forEach(el => {
    el.addEventListener('input', saveData);
});
</script>
