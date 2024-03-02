const chatInput = document.querySelector(".chat-input textarea");

const sendChatBtn = document.querySelector(".chat-input span");

const chatbox = document.querySelector(".chatbox");


const createChatLi = (message, className) => {

   // create a chat <li> element with passed message and className

   const chatLi = document.createElement("li");

   chatLi.classList.add("chat", className);

   const chatContent = className === "outgoing" ? `<p>${message}</p>` : `<img src="./smart_toy_FILL0_wght400_GRAD0_opsz24.png" alt="/" class="material-symbols-outlined">${message}`;

   chatLi.innerHTML = chatContent;

   return chatLi;

}


const handleChat = () => {

   const userMessage = chatInput.value.trim();

   if (!userMessage) return;

   // Append the user's message to the chatbox

   chatbox.appendChild(createChatLi(userMessage, "outgoing"));


   setTimeout(() => {

     // Display "thinking..." message while waiting for the response

     chatbox.appendChild(createChatLi("Thinking...","incoming"));


  }, 600);

}


sendChatBtn.addEventListener("click", handleChat);