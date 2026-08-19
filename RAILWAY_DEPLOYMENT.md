# Railway Deployment Guide

## Prerequisites
- GitHub account
- Railway account (sign up at https://railway.app with your GitHub account)

## Step 1: Push Backend Configuration to GitHub

The backend is now configured for Railway deployment with:
- `railway.json` - Railway build and deployment configuration
- `application-prod.yml` - Production configuration with environment variables
- Updated `SecurityConfig.java` - Dynamic CORS configuration

Commit and push these changes:
```bash
cd /home/govind/Desktop/project
git add backend/
git commit -m "Configure backend for Railway deployment"
git push origin main
```

## Step 2: Create Railway Project

1. Go to https://railway.app
2. Click **"Start a New Project"**
3. Select **"Deploy from GitHub repo"**
4. Choose your repository: **ManishVnskr/Expense_tracker**
5. Railway will detect your project

## Step 3: Add PostgreSQL Database

1. In your Railway project, click **"+ New"**
2. Select **"Database"** → **"Add PostgreSQL"**
3. Railway will automatically create a PostgreSQL database

## Step 4: Configure Backend Service

1. Click on your backend service
2. Go to **"Settings"** → **"Root Directory"**
   - Set to: `backend`
3. Go to **"Variables"** tab and add these environment variables:

### Required Environment Variables:

```bash
# Database (Railway will auto-populate these when you connect the database)
DATABASE_URL=<will be auto-filled by Railway>
DB_USERNAME=<will be auto-filled by Railway>
DB_PASSWORD=<will be auto-filled by Railway>

# JWT Secret (generate a secure random string)
JWT_SECRET=your-super-secure-256-bit-secret-key-change-this-immediately-make-it-random-and-long

# JWT Expiration (24 hours in milliseconds)
JWT_EXPIRATION=86400000

# CORS - Add your Netlify URL here (you'll update this after getting it)
CORS_ALLOWED_ORIGINS=https://expense-information.netlify.app,http://localhost:5173

# Spring Profile
SPRING_PROFILES_ACTIVE=prod

# Port (Railway uses PORT environment variable)
PORT=8080
```

## Step 5: Connect Database to Backend

1. In Railway dashboard, click on the **PostgreSQL** service
2. Click **"Connect"** button
3. Select your backend service
4. Railway will automatically inject database credentials as environment variables

## Step 6: Deploy Backend

1. Railway will automatically deploy when you push to GitHub
2. Or manually trigger deployment:
   - Go to your backend service
   - Click **"Deployments"** tab
   - Click **"Deploy"**

3. Wait for deployment to complete (usually 2-5 minutes)
4. Check deployment logs for any errors

## Step 7: Get Backend URL

1. Go to your backend service in Railway
2. Click **"Settings"**
3. Under **"Domains"**, click **"Generate Domain"**
4. Copy the generated URL (e.g., `https://expense-tracker-production.up.railway.app`)

## Step 8: Update Frontend Environment Variables

### For Netlify:

1. Go to your Netlify site: https://app.netlify.com/sites/expense-information
2. Click **"Site configuration"** → **"Environment variables"**
3. Add a new variable:
   - **Key**: `VITE_API_BASE_URL`
   - **Value**: `https://your-railway-url.railway.app/api/v1`
4. Click **"Save"**
5. Trigger a new deployment:
   - Go to **"Deploys"** → **"Trigger deploy"** → **"Deploy site"**

### For Local Development:

Update `frontend/.env`:
```bash
VITE_API_BASE_URL=https://your-railway-url.railway.app/api/v1
```

## Step 9: Update CORS in Railway

1. Go back to Railway backend service
2. Go to **"Variables"**
3. Update `CORS_ALLOWED_ORIGINS`:
   ```
   https://expense-information.netlify.app,http://localhost:5173
   ```
4. Save and redeploy

## Step 10: Verify Deployment

1. Open your Netlify site: https://expense-information.netlify.app
2. Try logging in with:
   - **Email**: john@example.com
   - **Password**: Test1234!
3. If the demo user doesn't exist, register a new account

## Troubleshooting

### Database Connection Issues
- Check that PostgreSQL service is running in Railway
- Verify `DATABASE_URL` is properly set
- Check deployment logs for connection errors

### CORS Errors
- Ensure your Netlify URL is in `CORS_ALLOWED_ORIGINS`
- Check that the URL doesn't have a trailing slash
- Redeploy after changing CORS settings

### 404 Errors
- Verify the `VITE_API_BASE_URL` includes `/api/v1`
- Check that backend is deployed and running
- Test backend health endpoint: `https://your-railway-url.railway.app/api/v1/auth/register`

### Demo User Not Found
The demo user is created by the `DataInitializer` on first startup. Check:
- Backend logs in Railway to see if initialization ran
- Database tables are created properly
- If needed, register a new account manually

## Cost & Limits

**Railway Free Tier:**
- $5 credit per month
- Sufficient for development/demo
- Monitor usage in Railway dashboard

**Estimated Monthly Usage:**
- Backend: ~$3-4
- PostgreSQL: ~$1-2

## Security Notes

⚠️ **Important**:
- Change the `JWT_SECRET` to a random, secure value
- Never commit secrets to GitHub
- Use Railway's environment variables for sensitive data
- Enable HTTPS only in production (Railway provides this automatically)

## Next Steps

1. Set up monitoring and alerts in Railway
2. Configure custom domain (optional)
3. Set up automatic backups for PostgreSQL
4. Add health check endpoints
5. Configure logging aggregation

---

**Need Help?**
- Railway Docs: https://docs.railway.app
- Railway Discord: https://discord.gg/railway
- Netlify Support: https://answers.netlify.com
