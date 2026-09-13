# Changelog

All notable changes to this project are documented in this file.

## [0.8.0]

### Added
- `backend/requirements.txt` with pinned dependency versions for reproducible backend installs
- `npm run dev:all` script (via `concurrently`) to start the backend and frontend together with one command
- User management in the admin panel: list registered users, change roles, delete accounts
- Admin can manually create user accounts (any role) from the admin panel
- `editor` role — can manage products but not users, orders, or messages
- Instant login right after signup, no separate sign-in step
- Company info section on the About page (address, phone, email) with an embedded Google Map pinned at Cara Dušana 15, Zemun
- Contact form on the About page, backed by a new `/contact` endpoint and stored in the database
- Admin "Messages" tab to view and delete submitted contact messages
- Real order persistence — checkout now submits orders to the backend instead of faking an order number client-side
- Admin "Orders" tab to view placed orders and their line items

### Changed
- Rewrote `README.md` to document the full stack, project structure, setup, and scripts
- Restored `.claude/launch.json` with a combined `dev` launch config alongside the existing `frontend`/`backend` ones
- Footer: removed placeholder "Sustainability"/"Careers" links and the unused social icon row (IG/TT/PIN)
- Footer "Contact" link now scrolls to the About page's contact section instead of going nowhere

### Fixed
- Product image not showing in the bag or checkout (cart items were reading a nonexistent `product.image` field instead of `product.images[0]`)

## [0.7.0] - 2026-08-16

### Added
- Admin panel for product management, product image galleries, per-size availability
- Discount tiers (10/20/30/40%) in the admin product form

### Changed
- Products now live in the database instead of a static file
- Product photos for the live catalog (denim, jeans, jacket, shorts)

## [0.6.0] - 2026-08-15

### Added
- Footer and moving bar at the top of the screen
- Backend connection for login and sign up buttons
- Product pages, checkout flow, category dropdown, real Google sign-in

### Changed
- Prices to RSD
- Mobile nav/grid fixes, session persistence, backend validation

## [0.5.0] - 2026-07-08

### Added
- Admin panel

### Changed
- Backend structure
- Product page updates

## [0.4.0] - 2026-01-28

### Added
- Flask backend of the application
- Profile page shown when a user is logged in, with a chart component
- Login and Sign up connected to the backend

### Changed
- Favicon
- Stopped tracking `backend/venv` and `backend/instance` in git

## [0.3.0] - 2026-01-23

### Added
- Login form and Sign up form
- Google Sign-In support

### Changed
- Styles of the Men and Women pages

## [0.2.0] - 2025-06-19

### Added
- Men and Women pages with category cards (Clothing, Footwear, Accessories)

### Changed
- Navigation bar style; removed Clothing/Footwear/Sale tabs, added Men/Women/Kids tabs

## [0.1.0] - 2025-06-18

### Added
- Home page header and background image
- About page content: generated text, address, phone number, email
- Google Maps embed on the About page
- `CHANGELOG.md`
