


// Get Stripe publishable key
fetch("http://localhost:3000/api/stripe/publishable-key", {
  method: "GET",
  headers: {
    "Content-Security-Policy": "sandbox allow-scripts allow-same-origin",
  }
})
  .then((result) => { return result.json(); })
  .then((data) => {
    emailInput = document.querySelector("#email");
    console.log(data);
    // Initialize Stripe.js
    const stripe = Stripe(data.publishable_key);
    document.querySelector("#checkout-button-1").addEventListener("click", () => {
      // Get Checkout Session ID
      fetch("http://localhost:3000/api/stripe/create-checkout-session", {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify({
          "productId": "temporary",
          "email": emailInput.value
        })
      })
        .then((result) => { return result.json(); })
        .then((data) => {
          console.log(data);
          // Redirect to Stripe Checkout
          return stripe.redirectToCheckout({ sessionId: data.session_id }); // Add allow_same_origin here
        })
        .then((res) => {
          console.log(res);
        });
    });

     document.querySelector("#checkout-button-2").addEventListener("click", () => {
      // Get Checkout Session ID
      fetch("http://localhost:3000/api/stripe/create-checkout-session", {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify({
          "productId": "unique",
          "email": emailInput.value
        })
      })
        .then((result) => { return result.json(); })
        .then((data) => {
          console.log(data);
          // Redirect to Stripe Checkout
          return stripe.redirectToCheckout({ sessionId: data.session_id }); // Add allow_same_origin here
        })
        .then((res) => {
          console.log(res);
        });
    });
    document.querySelector("#checkout-button-3").addEventListener("click", () => {
      // Get Checkout Session ID
      fetch("http://localhost:3000/api/stripe/create-checkout-session", {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify({
          "productId": "multiple",
          "email": emailInput.value
        })
      })
        .then((result) => { return result.json(); })
        .then((data) => {
          console.log(data);
          // Redirect to Stripe Checkout
          return stripe.redirectToCheckout({ sessionId: data.session_id }); // Add allow_same_origin here
        })
        .then((res) => {
          console.log(res);
        });
        
    });
  });