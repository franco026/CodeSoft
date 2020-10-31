import React from 'react';

function Footer() {
	return (
		<nav className="navbar fixed-buttom navbar-dark bg-dark" style={{ backgroundColor: 'black', color: 'white' , width:'100%', height:'100%'}}>
			<p>&copy; {(new Date().getFullYear())} CodeSoft, Inc.</p>
		</nav>
	);
}

export default Footer;