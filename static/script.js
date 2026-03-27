document.getElementById("form").addEventListener("submit", async function(e) {
    e.preventDefault();

    let age = document.getElementById("age").value;
    let premium = document.getElementById("premium").value;
    let vehicle_age = document.getElementById("vehicle_age").value;

    let res = await fetch("/predict", {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify({
            age: age,
            premium: premium,
            vehicle_age: vehicle_age
        })
    });

    let data = await res.json();

    let result = document.getElementById("result");
    let bar = document.getElementById("progress");

    let prob = data.probability;

    bar.style.width = prob + "%";

    if (data.prediction === 1) {
        result.innerHTML = "⚠️ High Claim Risk (" + prob + "%)";
        bar.style.background = "red";
    } else {
        result.innerHTML = "✅ Low Claim Risk (" + prob + "%)";
        bar.style.background = "green";
    }
});