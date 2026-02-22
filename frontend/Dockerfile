# Image Node.js pour installer les outils React
FROM node:18-slim

WORKDIR /app

# On copie la liste des besoins (package.json)
COPY package.json .

# On installe React et ses outils
RUN npm install

# On copie ton code App.js
COPY . .

# On lance le serveur de développement
CMD ["npm", "start"]
