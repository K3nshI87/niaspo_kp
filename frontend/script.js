document.getElementById("policy-form").addEventListener("submit", async (event) => {
    event.preventDefault();

    const name = document.getElementById("name").value;
    const city = document.getElementById("city").value;
    const policyType = document.getElementById("policy-type").value;

    // URL бэкенда (Теперь указываем локальный сервер или адрес контейнера)
    const backendUrl = "http://localhost:5000/policy/";

    try {
        const response = await fetch(backendUrl, {
            method: "POST",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify({
                name,
                city,
                policy_type: policyType
            })
        });

        if (response.ok) {
            const result = await response.json();
            document.getElementById("result").innerText = `Полис успешно оформлен: ${result.policy_id}`;
        } else {
            document.getElementById("result").innerText = "Ошибка при оформлении полиса!";
        }
    } catch (error) {
        console.error("Error during fetch:", error);  // Подробная ошибка в консоли
        document.getElementById("result").innerText = "Ошибка соединения с сервером!";
    }
});
