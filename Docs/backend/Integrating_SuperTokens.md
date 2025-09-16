# Integrating SuperTokens

Integrating SuperTokens with a Vue.js frontend and a FastAPI backend involves configuring both the client-side and server-side to use the SuperTokens SDK and manage authentication.


1. SuperTokens Core Setup:

- Obtain SuperTokens Core credentials (Connection URI and API key) by creating an account and setting up an application core on the SuperTokens website. This core handles the actual authentication logic.


2. FastAPI Backend Integration:

- **Install SuperTokens SDK:** 
    
    Install the `supertokens-python` library in your FastAPI project.
    
- **Initialize SuperTokens:** 
    
    In your main FastAPI application file, initialize the SuperTokens SDK with your `connectionURI`, `api_key`, and `appInfo` (including `appName`, `apiDomain`, `websiteDomain`, `apiBasePath`, and `websiteBasePath`).
    
- **Add Recipes:** 
    
    Include the desired authentication recipes (e.g., `Session`, `EmailPassword`) in the SuperTokens initialization.
    
- **CORS Configuration:** 
    
    Configure CORS in your FastAPI application to allow requests from your Vue.js frontend domain.
    
- **SuperTokens Middleware:** 
    
    Add the SuperTokens middleware to your FastAPI application to expose authentication API routes (like sign-up, sign-in, sign-out).
    
- **Error Handling:** 
    
    Implement SuperTokens' error handling to manage authentication-related errors gracefully.
    

3. Vue.js Frontend Integration:

- **Install SuperTokens SDK:** 
    
    Install the `supertokens-web-js` library in your Vue.js project. If using a pre-built UI, you might also install `supertokens-auth-react` (though the pre-built UI can also be loaded via CDN).
    
- **Initialize SuperTokens:** 
    
    In your `main.js` or a dedicated authentication setup file, initialize the SuperTokens SDK with `appInfo` (matching the backend configuration) and the `recipeList` containing the same recipes as the backend.
    
- **Authentication UI:**
    
    - **Pre-built UI:** If using the pre-built UI, load the SuperTokens UI script from the CDN and render it in a designated HTML element within your Vue component.
    - **Custom UI:** If building a custom UI, use the `supertokens-web-js` SDK methods (e.g., `EmailPassword.signUp`, `EmailPassword.signIn`) to interact with the backend authentication endpoints.
    
- **Session Management:** 
    
    Wrap your application with the `SuperTokensWrapper` component (if using React-based pre-built UI) or manually manage session tokens using the `supertokens-web-js` SDK for custom UIs.
    
- **Protected Routes:** 
    
    Implement route guards in Vue Router to protect routes based on the user's authentication status (e.g., using `Session.doesSessionExist()`).
    

4. Protecting Backend Routes:

- Use SuperTokens' session verification middleware in your FastAPI routes to ensure that only authenticated users can access specific endpoints.

By following these steps, you can successfully integrate SuperTokens for secure and efficient authentication in your Vue.js and FastAPI application.



