const predictBtn = document.getElementById("predictBtn");

predictBtn.addEventListener("click", predictRisk);

async function predictRisk() {

    const discount = parseFloat(document.getElementById("discount").value);

    const rating = parseFloat(document.getElementById("rating").value);

    const ratingCount = parseInt(document.getElementById("ratingCount").value);

    const actualPrice = parseFloat(document.getElementById("actualPrice").value);

    const discountedPrice = parseFloat(document.getElementById("discountedPrice").value);

    if (
        isNaN(discount) ||
        isNaN(rating) ||
        isNaN(ratingCount) ||
        isNaN(actualPrice) ||
        isNaN(discountedPrice)
    ) {

        alert("Please fill all fields.");

        return;

    }

    predictBtn.innerHTML =
        '<i class="fa-solid fa-spinner fa-spin"></i> Analyzing...';

    predictBtn.disabled = true;

    try {

        const response = await fetch(
            "https://darkpatternplatform.onrender.com/predict",
            {

                method: "POST",

                headers: {

                    "Content-Type": "application/json"

                },

                body: JSON.stringify({

                    discount_percentage: discount,

                    rating: rating,

                    rating_count: ratingCount,

                    actual_price: actualPrice,

                    discounted_price: discountedPrice

                })

            }
        );

        const data = await response.json();

        showResult(data);

    }catch (error) {
    console.error("Fetch Error:", error);
    alert(error.message);
}

    predictBtn.innerHTML =
        '<i class="fa-solid fa-wand-magic-sparkles"></i> Analyze Product';

    predictBtn.disabled = false;

}

function showResult(data) {

    const badge = document.getElementById("riskBadge");

    const confidence = document.getElementById("confidence");

    const progress = document.getElementById("progressBar");

    const recommendation = document.getElementById("recommendation");

    const score = document.getElementById("score");

    badge.classList.remove("low");
    badge.classList.remove("medium");
    badge.classList.remove("high");

    badge.innerHTML = data.RiskLevel.toUpperCase();

    if (data.RiskLevel.toLowerCase() === "low") {

        badge.classList.add("low");

        recommendation.innerHTML =
            "✅ Safe Product<br><br>This product shows very few dark pattern indicators.";

    }

    else if (data.RiskLevel.toLowerCase() === "medium") {

        badge.classList.add("medium");

        recommendation.innerHTML =
            "⚠ Moderate Risk<br><br>Review product carefully before purchasing.";

    }

    else {

        badge.classList.add("high");

        recommendation.innerHTML =
            "🚨 High Risk Detected<br><br>Very high discount or suspicious product behaviour detected.";

    }

    confidence.innerHTML =
        "Confidence : " + data.Confidence + "%";

    progress.style.width =
        data.Confidence + "%";

    score.innerHTML =
        Math.round(data.Confidence);

}