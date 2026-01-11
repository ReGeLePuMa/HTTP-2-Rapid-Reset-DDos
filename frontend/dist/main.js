window.onload = () => {
    const btn = document.getElementById("generate-button");
    const image = document.getElementById("art-image");
    const artContainer = document.getElementById("art-container");
    btn.onclick = async () => {
        btn.disabled = true;
        btn.innerText = "Generating...";
        btn.classList.remove("cursor-pointer");
        btn.classList.add("opacity-50", "cursor-not-allowed");
        
        const response = await fetch("/api/image");
        if (!response.ok) {
            Swal.fire({
                icon: "error",
                title: "Error",
                text: "Failed to generate art. Please try again later.",
                timer: 3000
            });
        } else {
            const blob = await response.blob();
            const imageUrl = URL.createObjectURL(blob);
            image.onload = () => URL.revokeObjectURL(image.src);
            image.src = imageUrl;
            artContainer.classList.remove("hidden");
        }
        btn.disabled = false;
        btn.innerText = "Generate Art";
        btn.classList.remove("opacity-50", "cursor-not-allowed");
        btn.classList.add("cursor-pointer");
    };
};
