document.addEventListener("DOMContentLoaded", function () {

    const forms = document.querySelectorAll("form");

    forms.forEach(form => {

        form.addEventListener("submit", function () {

            const overlay = document.createElement("div");

            overlay.id = "loadingOverlay";

            overlay.innerHTML = `
                <div style="
                    position:fixed;
                    top:0;
                    left:0;
                    width:100%;
                    height:100%;
                    background:rgba(255,255,255,.92);
                    display:flex;
                    justify-content:center;
                    align-items:center;
                    flex-direction:column;
                    z-index:9999;
                    font-family:Segoe UI;
                ">
                    <h2>🎥</h2>
                    <h3>Analyzing Video...</h3>
                    <p>Please wait...</p>
                </div>
            `;

            document.body.appendChild(overlay);

        });

    });

});