# Quick Start: Deploy to Railway

## ✅ What's Done
- Backend is configured for Railway deployment
- Railway configuration files are pushed to GitHub
- CORS is set up to accept your Netlify frontend
- Environment variable support is added

## 🚀 Next Steps (Follow These in Order)

### Step 1: Create Railway Account & Deploy Backend (15 minutes)

1. **Sign up for Railway**
   - Go to https://railway.app
   - Click "Login with GitHub"
   - Authorize Railway

2. **Create New Project**
   - Click "Start a New Project"
   - Select "Deploy from GitHub repo"
   - Choose: `ManishVnskr/Expense_tracker`
   - Railway will start building

3. **Set Root Directory**
   - Click on your service
   - Go to "Settings" tab
   - Find "Root Directory" 
   - Set to: `backend`
   - Click "Update"

4. **Add PostgreSQL Database**
   - In your project dashboard, click "+ New"
   - Select "Database" → "Add PostgreSQL"
   - Wait for database to be created

5. **Connect Database to Backend**
   - Click on the PostgreSQL service
   - Click "Connect" 
   - Select your backend service
   - Railway will inject database credentials automatically

6. **Add Environment Variables**
   - Click on your backend service
   - Go to "Variables" tab
   - Click "Add Variable" and add these:

   ```
   SPRING_PROFILES_ACTIVE=prod
   JWT_SECRET=change-this-to-a-very-long-random-string-at-least-64-characters-long
   CORS_ALLOWED_ORIGINS=https://expense-information.netlify.app,http://localhost:5173
   ```

   Note: Railway automatically provides:
   - `DATABASE_URL`
   - `PORT`

7. **Generate Domain**
   - In Settings tab, scroll to "Domains"
   - Click "Generate Domain"
   - Copy the URL (e.g., `expense-tracker-production-xxxx.up.railway.app`)
   - **SAVE THIS URL** - you'll need it next!

8. **Wait for Deployment**
   - Go to "Deployments" tab
   - Wait for build to complete (green checkmark)
   - Check logs for "Started ExpenseTrackerApplication"

### Step 2: Update Netlify Frontend (5 minutes)

1. **Add Environment Variable to Netlify**
   - Go to https://app.netlify.com/sites/expense-information
   - Click "Site configuration" → "Environment variables"
   - Click "Add a variable"
   - Key: `VITE_API_BASE_URL`
   - Value: `https://your-railway-domain.railway.app/api/v1`
     (Replace with your Railway URL from Step 1.7)
   - Click "Create variable"

2. **Trigger New Deploy**
   - Go to "Deploys" tab
   - Click "Trigger deploy" → "Deploy site"
   - Wait for deployment to complete

### Step 3: Test Your Application (2 minutes)

1. **Open Your Site**
   - Go to: https://expense-information.netlify.app

2. **Register a New Account** (Demo user might not exist yet)
   - Click "Register" or "Sign Up"
   - Create an account with:
     - Email: your@email.com
     - Password: Test1234!
     - Full Name: Your Name

3. **Or Try Demo Account** (if it exists)
   - Email: john@example.com
   - Password: Test1234!

4. **Test Features**
   - Create a transaction
   - View dashboard
   - Check analytics

## 🐛 Troubleshooting

### Backend Won't Deploy
- Check "Deployments" → "View Logs"
- Look for Java version errors (should use Java 17)
- Check if database is connected

### Frontend Can't Connect to Backend
- Verify `VITE_API_BASE_URL` is correct in Netlify
- Check Railway backend is running (green status)
- Test backend directly: `https://your-railway-url.railway.app/api/v1/auth/register`

### CORS Errors
- Make sure `CORS_ALLOWED_ORIGINS` includes your Netlify URL
- No trailing slashes in URLs
- Redeploy backend after changing CORS

### Login Fails
- Try registering a new account instead
- Check Railway logs for database connection issues
- Verify Flyway migrations ran successfully

## 💰 Cost Estimate

**Railway Free Tier:**
- $5 credit per month
- Backend: ~$3/month
- PostgreSQL: ~$1/month
- Should be sufficient for demo/development

**Netlify:**
- Free tier (more than enough for this app)

## 📝 Important Notes

- Railway may take 3-5 minutes to build and deploy
- First request to backend may be slow (cold start)
- Demo user is created on first backend startup
- Always use HTTPS URLs (Railway provides this)

## ❓ Need Help?

See the full guide: `RAILWAY_DEPLOYMENT.md`

Railway Support: https://discord.gg/railway
Netlify Support: https://answers.netlify.com

---

**Once everything is deployed, you'll have:**
- ✅ Frontend: https://expense-information.netlify.app
- ✅ Backend: https://your-railway-url.railway.app
- ✅ Database: PostgreSQL on Railway
- ✅ Full-stack app running in the cloud!
