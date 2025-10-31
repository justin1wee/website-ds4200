# Personal Website - GitHub Pages

This is a personal website built with HTML and CSS, designed to be deployed on GitHub Pages.

## Files Included

- `index.html` - Home page with introduction and contact information
- `about.html` - Second page with more detailed information and interests
- `styles.css` - Custom CSS styling with modern design
- `README.md` - This file

## Features

✅ Two-page website structure  
✅ Custom typography (Inter and Playfair Display fonts)  
✅ Modern color scheme  
✅ Responsive design  
✅ Navigation menu  
✅ Contact section with social media links  

## Deploying to GitHub Pages

Follow these steps to publish your website on GitHub Pages:

### Step 1: Create a GitHub Repository

1. Go to [GitHub](https://github.com) and sign in
2. Click the "+" icon in the top right corner
3. Select "New repository"
4. Name your repository (e.g., `my-personal-website` or `username.github.io`)
5. Make it **Public** (required for free GitHub Pages)
6. **Do NOT** initialize with a README (you already have one)
7. Click "Create repository"

### Step 2: Upload Your Files

**Option A: Using Git (Recommended)**

1. Open Terminal/Command Prompt
2. Navigate to your project folder:
   ```bash
   cd /Users/justin/Documents/DS4200/Homework3
   ```
3. Initialize git (if not already done):
   ```bash
   git init
   ```
4. Add all files:
   ```bash
   git add .
   ```
5. Commit the files:
   ```bash
   git commit -m "Initial commit: Personal website"
   ```
6. Add your GitHub repository as remote (replace `YOUR_USERNAME` and `YOUR_REPO_NAME`):
   ```bash
   git remote add origin https://github.com/YOUR_USERNAME/YOUR_REPO_NAME.git
   ```
7. Push to GitHub:
   ```bash
   git branch -M main
   git push -u origin main
   ```

**Option B: Using GitHub Web Interface**

1. Go to your newly created repository on GitHub
2. Click "uploading an existing file"
3. Drag and drop all your files (`index.html`, `about.html`, `styles.css`)
4. Add a commit message: "Initial commit: Personal website"
5. Click "Commit changes"

### Step 3: Enable GitHub Pages

1. In your repository, go to **Settings** (top menu)
2. Scroll down to **Pages** in the left sidebar
3. Under **Source**, select:
   - Branch: `main` (or `master` if you used that)
   - Folder: `/ (root)`
4. Click **Save**
5. GitHub will provide a URL like: `https://YOUR_USERNAME.github.io/YOUR_REPO_NAME/`

### Step 4: Access Your Website

- Wait 1-2 minutes for GitHub to build your site
- Visit your site at the URL provided by GitHub
- Your website should now be live!

## Important Notes

⚠️ **Custom Domain (Optional)**: If you want a custom domain like `yourname.com`, you can configure it in the Pages settings, but this is not required for the assignment.

⚠️ **Update Contact Links**: Remember to update the email and social media links in `index.html` with your actual contact information before submitting.

⚠️ **Testing**: Make sure to test all navigation links and verify that both pages load correctly on your GitHub Pages site.

## Local Testing

To preview your website locally before deploying:

1. Open `index.html` in a web browser
2. Or use a local server:
   ```bash
   # Python 3
   python3 -m http.server 8000
   
   # Then visit: http://localhost:8000
   ```

## Customization

Feel free to customize:
- Text content in both HTML files
- Colors in `styles.css` (see `:root` variables)
- Images (replace the Unsplash URLs with your own)
- Contact information and social links

## Troubleshooting

**Problem**: Website doesn't load  
**Solution**: Make sure you selected the correct branch and root folder in Pages settings

**Problem**: Images don't show  
**Solution**: Check image URLs are correct and accessible (or use relative paths for local images)

**Problem**: Links don't work  
**Solution**: Ensure all file paths use relative paths (e.g., `./about.html` not absolute paths)

---

Good luck with your assignment! 🚀

