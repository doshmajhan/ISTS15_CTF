<?php
/**
 * The base configuration for WordPress
 *
 * The wp-config.php creation script uses this file during the
 * installation. You don't have to use the web site, you can
 * copy this file to "wp-config.php" and fill in the values.
 *
 * This file contains the following configurations:
 *
 * * MySQL settings
 * * Secret keys
 * * Database table prefix
 * * ABSPATH
 *
 * @link https://codex.wordpress.org/Editing_wp-config.php
 *
 * @package WordPress
 */

// ** MySQL settings - You can get this info from your web host ** //
/** The name of the database for WordPress */
define('DB_NAME', 'wordpress');

/** MySQL database username */
define('DB_USER', 'wpuser');

/** MySQL database password */
define('DB_PASSWORD', 'FIj54p5n7iwCrHSEQsiK');

/** MySQL hostname */
define('DB_HOST', 'localhost');

/** Database Charset to use in creating database tables. */
define('DB_CHARSET', 'utf8mb4');

/** The Database Collate type. Don't change this if in doubt. */
define('DB_COLLATE', '');

/**#@+
 * Authentication Unique Keys and Salts.
 *
 * Change these to different unique phrases!
 * You can generate these using the {@link https://api.wordpress.org/secret-key/1.1/salt/ WordPress.org secret-key service}
 * You can change these at any point in time to invalidate all existing cookies. This will force all users to have to log in again.
 *
 * @since 2.6.0
 */
define('AUTH_KEY',         '}dz:]7Yp/LBZQ@!&(!`oQR )*kS/O}z1_SmlOI1yP?dh#Wi|Bw64Yxs6%:R{^u&*');
define('SECURE_AUTH_KEY',  'r.]SV=wzcWEzf9ZcKsOJHcCR)o3g9=@1@nYFV+!j=T<}J4zR)`*r?-#]#r!H`{.u');
define('LOGGED_IN_KEY',    'P)r}4]W461]~%W>_fM$yBa[xMf}w|K$9RhZXGWL!/37JhQ:ta<Vy.g3@.J4@rt0W');
define('NONCE_KEY',        'Wzw*O+i-K9P[.JbaNeOC:zr<$W;<Ln8IUAQB}.6ptFm4|1G}XBmJ]@zG~AKQXD:K');
define('AUTH_SALT',        '_85i(#o?f[EX%#BW_8YJB3WWkC`qkoT?ZJ0Z,=h:b90lUI(F/b0-V6(]Dm,7#s)=');
define('SECURE_AUTH_SALT', 'X lp[w&qw6upkIsZ~&(SH]>[G^l0zCXyN8 h_~)Nhh72p=}PWobPp3A}4nkrXGzb');
define('LOGGED_IN_SALT',   'rnj@]fqpodZ3^W^:e>^d$,C8]KOuJO[5;hr]Y,F6L@xJaHrUQ%lF_Gw#a+cX[}Y<');
define('NONCE_SALT',       ',2E=ZLSkz].8A_+$N0w#H(w<3GQ|(.;EE@e$7gf=JLB<pI;G3|#&F-%RW>AF-f|6');

/**#@-*/

/**
 * WordPress Database Table prefix.
 *
 * You can have multiple installations in one database if you give each
 * a unique prefix. Only numbers, letters, and underscores please!
 */
$table_prefix  = 'wp_';

/**
 * For developers: WordPress debugging mode.
 *
 * Change this to true to enable the display of notices during development.
 * It is strongly recommended that plugin and theme developers use WP_DEBUG
 * in their development environments.
 *
 * For information on other constants that can be used for debugging,
 * visit the Codex.
 *
 * @link https://codex.wordpress.org/Debugging_in_WordPress
 */
define('WP_DEBUG', false);

/* That's all, stop editing! Happy blogging. */

/** Absolute path to the WordPress directory. */
if ( !defined('ABSPATH') )
	define('ABSPATH', dirname(__FILE__) . '/');

/** Sets up WordPress vars and included files. */
require_once(ABSPATH . 'wp-settings.php');