document.addEventListener('DOMContentLoaded', function () {
    const divisions = document.querySelectorAll('.activity-text');
    const bgInfo = document.querySelector('.bg-info');
    let currentIndex = 0;

    function switchDivision() {
        // Fade out all divisions
        divisions.forEach((division) => {
            division.style.opacity = '0';
        });

        // Wait for fade out to complete, then show the next division
        setTimeout(() => {
            // Hide all divisions to prevent overlap
            divisions.forEach((division) => {
                division.style.display = 'none';
            });

            // Show the current division
            divisions[currentIndex].style.display = 'block';
            divisions[currentIndex].style.opacity = '1';

            // Move to the next division
            currentIndex = (currentIndex + 1) % divisions.length;
        }, 1000); // Match the transition duration (1s)
    }

    // Initial display
    divisions[currentIndex].style.display = 'block';
    divisions[currentIndex].style.opacity = '1';

    // Change division every 3 seconds
    const interval = setInterval(switchDivision, 3000);

    // Add click event listener to bg-info
    bgInfo.addEventListener('click', () => {
        // Stop automatic switching temporarily
        clearInterval(interval);
        switchDivision();
    });
});


document.addEventListener('DOMContentLoaded', function () {
    const scrollElements = document.querySelectorAll('.scroll-animation');

    const elementInView = (el, offset = 1) => {
        const elementTop = el.getBoundingClientRect().top;
        return (
            elementTop <= 
            (window.innerHeight || document.documentElement.clientHeight) / offset
        );
    };

    const displayScrollElement = (element) => {
        element.classList.add('visible');
    };

    const handleScrollAnimation = () => {
        scrollElements.forEach((el) => {
            if (elementInView(el, 1.25)) {
                displayScrollElement(el);
            }
        });
    };

    window.addEventListener('scroll', handleScrollAnimation);
});