#!/usr/bin/python
print "<!DOCTYPE html>
<html dir=\"ltr\" lang=\"en-US\">
<head>

	<meta http-equiv=\"content-type\" content=\"text/html; charset=utf-8\" />
	<meta name=\"author\" content=\"The Professional Recruiter\" />

	<!-- Stylesheets
	============================================= -->
	<link href=\"https://fonts.googleapis.com/css?family=Open+Sans:300,400,700\" rel=\"stylesheet\">
	<link rel=\"stylesheet\" href=\"css/bootstrap.css\" type=\"text/css\" />
	<link rel=\"stylesheet\" href=\"style.css\" type=\"text/css\" />
	<link rel=\"stylesheet\" href=\"css/swiper.css\" type=\"text/css\" />
	<link rel=\"stylesheet\" href=\"css/dark.css\" type=\"text/css\" />
	<link rel=\"stylesheet\" href=\"css/font-icons.css\" type=\"text/css\" />
	<link rel=\"stylesheet\" href=\"css/animate.css\" type=\"text/css\" />
	<link rel=\"stylesheet\" href=\"css/magnific-popup.css\" type=\"text/css\" />
	<link rel=\"icon\" href=\"favicon.png\" type=\"image/png\" sizes=\"16x16\">
	<link rel=\"stylesheet\" href=\"css/responsive.css\" type=\"text/css\" />
	<meta name=\"viewport\" content=\"width=device-width, initial-scale=1\" />
	<!--[if lt IE 9]>
		<script src=\"http://css3-mediaqueries-js.googlecode.com/svn/trunk/css3-mediaqueries.js\"></script>
	<![endif]-->

	<!-- Document Title
	============================================= -->
	<title>Home - The Professional Recruiter</title>
<script type=\"text/javascript\" src=\"https://maps.googleapis.com/maps/api/js\"></script>
        
        <script type=\"text/javascript\">
            // When the window has finished loading create our google map below
            google.maps.event.addDomListener(window, 'load', init);
        
            function init() {
                
				
				// Basic options for a simple Google Map
                // For more options see: https://developers.google.com/maps/documentation/javascript/reference#MapOptions
                var mapOptions = {
                    // How zoomed in you want the map to start at (always required)
                    zoom: 17,

                    // The latitude and longitude to center the map (always required)
                    center: new google.maps.LatLng(-31.887260, 115.999700), // New York

                    // How you would like to style the map. 
                    // This is where you would paste any style found on Snazzy Maps.
 styles: [{\"stylers\":[{\"saturation\":-100},{\"gamma\":0.8},{\"lightness\":4},{\"visibility\":\"on\"}]},{\"featureType\":\"landscape.natural\",\"stylers\":[{\"visibility\":\"on\"},{\"color\":\"#ffffff\"},{\"gamma\":6.97},{\"lightness\":-5},{\"saturation\":100}]}]
                };

                // Get the HTML DOM element that will contain your map 
                // We are using a div with id=\"map\" seen below in the <body>
                var mapElement = document.getElementById('map');

                // Create the Google Map using our element and options defined above
                var map = new google.maps.Map(mapElement, mapOptions);

                // Let's also add a marker while we're at it
			var image = 'images/marker.png';
			  var beachMarker = new google.maps.Marker({
				position: {lat: -31.887260, lng: 115.999700}, 
				map: map,
				icon: image,
				title: 'The Professional Recruiter'
			  });
            }
        </script>
</head>

<body class=\"stretched\">

	<!-- Document Wrapper
	============================================= -->
	<div id=\"wrapper\" class=\"clearfix\">

		<!-- Header
		============================================= -->
		<header id=\"header\" class=\"full-header\">

			<div id=\"header-wrap\">

				<div class=\"container clearfix\">

					<div id=\"primary-menu-trigger\"><i class=\"icon-reorder\"></i></div>

					<!-- Logo
					============================================= -->
					<div id=\"logo\">
						<a href=\"index.html\" class=\"standard-logo\" data-dark-logo=\"images/logo-dark.png\"><img src=\"images/logo.png\" alt=\"Canvas Logo\"></a>
						<a href=\"index.html\" class=\"retina-logo\" data-dark-logo=\"images/logo-dark@2x.png\"><img src=\"images/logo@2x.png\" alt=\"Canvas Logo\"></a>
					</div><!-- #logo end -->

					<!-- Primary Navigation
					============================================= -->
					<nav id=\"primary-menu\">

						<ul>
							<li class=\"current\"><a href=\"index.html\"><div>Home</div></a></li>
							<li><a href=\"about_us.html\"><div>About Us</div></a></li>
							<li><a href=\"our_service.html\"><div>Our Service</div></a></li>
							<li><a href=\"contact.html\"><div>Contact Us</div></a></li>
						</ul>

						<!-- Top Search
						============================================= -->
						<div class=\"menubar\"></div>

					</nav><!-- #primary-menu end -->
				</div>

			</div>

		</header><!-- #header end -->


<div class=\"swiperBub\"></div>
		<section id=\"slider\" class=\"slider-parallax swiper_wrapper clearfix\" data-loop=\"true\" data-autoplay=\"3000\">
		<div class=\"menuBorder\"></div>
			<div class=\"slider-parallax-inner\">
				<div class=\"swiper-container swiper-parent\">
				<div class=\"swiperMask\"><img src=\"images/slider/swiper/mask.png\"></div>

				<div class=\"swiperBub2\"></div>
				<div class=\"swiperBub3\"></div>
					<div class=\"swiper-wrapper\">
					
						<div class=\"swiper-slide dark\" style=\"background-image: url('images/slider/swiper/1.jpg');\" onClick=\"location.href='about_us.html';\">
							<div class=\"container clearfix\">
								<div class=\"slider-caption slider-caption-center\">
								<div class=\"welcomeBox\" data-caption-animate=\"fadeInDown\" data-caption-delay=\"0\">Welcome to The Professional Recruiter</div>
									<h2 data-caption-animate=\"fadeInUp\" data-caption-delay=\"0\">Your Difficulties<br/>We Solve</h2>
									<div class=\"cta\" data-caption-animate=\"fadeInUp\" data-caption-delay=\"400\"><a href=\"about_us.html\" target=\"_parent\">Explore more</a></div>
								</div>
							</div>
						</div>
						<div class=\"swiper-slide dark\" style=\"background-image: url('images/slider/swiper/2.jpg');\" onClick=\"location.href='about_us.html';\">
							<div class=\"container clearfix\">
								<div class=\"slider-caption slider-caption-center\">
								<div class=\"welcomeBox\" data-caption-animate=\"fadeInDown\" data-caption-delay=\"0\">Welcome to The Professional Recruiter</div>
									<h2 data-caption-animate=\"fadeInUp\" data-caption-delay=\"0\">Your Prospects<br/>We Care</h2>
									<div class=\"cta\" data-caption-animate=\"fadeInUp\" data-caption-delay=\"400\"><a href=\"about_us.html\" target=\"_parent\">Explore more</a></div>
								</div>
							</div>
						</div>
						<div class=\"swiper-slide dark\" style=\"background-image: url('images/slider/swiper/3.jpg');\" onClick=\"location.href='about_us.html';\">
							<div class=\"container clearfix\">
								<div class=\"slider-caption slider-caption-center\">
								<div class=\"welcomeBox\" data-caption-animate=\"fadeInDown\" data-caption-delay=\"0\">Welcome to The Professional Recruiter</div>
									<h2 data-caption-animate=\"fadeInUp\" data-caption-delay=\"0\">The right person, the right place, <br/>at the right time</h2>
									<div class=\"cta\" data-caption-animate=\"fadeInUp\" data-caption-delay=\"400\"><a href=\"about_us.html\" target=\"_parent\">Explore more</a></div>
								</div>
							</div>
						</div>
					</div>
					<div id=\"slider-arrow-left\"><i class=\"icon-angle-left\"></i></div>
					<div id=\"slider-arrow-right\"><i class=\"icon-angle-right\"></i></div>
					<!--div id=\"slide-number\"><div id=\"slide-number-current\"></div><span>/</span><div id=\"slide-number-total\"></div></div-->
					<div class=\"swiper-pagination\"></div>
				</div>
			</div>
		</section>
		
<section id=\"content\">
	<div class=\"content-wrap\" style=\"padding-bottom:0;\">
		<div class=\"container clearfix\" style=\"padding-bottom:80px;\">
		<h4 class=\"heading\">Our Expertises</h4>
					<div class=\"col_one_third nobottommargin\">
						<div class=\"feature-box fbox-center fbox-light fbox-effect nobottomborder\">
							<div class=\"fbox-icon\">
								<img src=\"images/icon01.png\" style=\"height:92px; width:92px;\">
							</div>
							<h3>Permanent Job Placement</h3>
						</div>
					</div>

					<div class=\"col_one_third nobottommargin\">
						<div class=\"feature-box fbox-center fbox-light fbox-effect nobottomborder\">
							<div class=\"fbox-icon\">
								<img src=\"images/icon02.png\" style=\"height:92px; width:92px;\">
							</div>
							<h3 class=\"superWide\">Mass Recruitment Project / Secondment Services</h3>
						</div>
					</div>


					<div class=\"col_one_third nobottommargin col_last\">
						<div class=\"feature-box fbox-center fbox-light fbox-effect nobottomborder\">
							<div class=\"fbox-icon\">
								<img src=\"images/icon03.png\" style=\"height:92px; width:92px;\">
							</div>
							<h3>Temporary / Contract Staffing</h3>
						</div>
					</div>
		</div>
		
		<div class=\"section parallax nomargin notopborder dark\" style=\"background-image: url('images/parallax/2.jpg'); padding: 100px 0;\" data-stellar-background-ratio=\"0.3\">
					<div class=\"container clearfix\">
					<h4 class=\"heading\">Why The Professional Recruiter</h4>
					<div class=\"centerLine\"></div>
					<div class=\"backetLine\"></div>
						<div class=\"row\">
							<div class=\"col-md-4 bottommargin\">
								<div class=\"testimonial\">
									<div class=\"testi-content\">
									<span>Extensive Talent Pool</span>
										<p>We are constantly building personal networks with various candidates in Australia, and able to approach special and silent job 
seekers. And we keep extending sourcing channels by holding seminars and recruitment talk in education institutes and exhibitions.</p>
									</div>
								</div>
							</div>

							<div class=\"col-md-4 bottommargin\">
								<div class=\"testimonial\">
									<div class=\"testi-content\">
									<span>Proven Track Record</span>
										<p>We have a proven track record in 
delivering best-fit talents for some of the multinational companies across various industries. It is a clear indicator which we are confident of successfully matching job-seekers to vacancies.</p>
									</div>
								</div>
							</div>
							
							<div class=\"col-md-4 bottommargin\">
								<div class=\"testimonial\">
									<div class=\"testi-content\">
									<span>Reliable Services</span>
										<p>Our business consultants are trained to work very closely with clients, from requirement gathering, candidate seraching, interview management to after care services. The major purpose is to ensure that the result can meet the clients’ ultimate objectives.</p>
									</div>
								</div>
							</div>
					
						</div>
			<div class=\"backetLineBottom\"></div>
					</div>
			  </div>
			  
	<div class=\"clearfix\" style=\"padding:80px 0 0 0; width:100%; margin:0;\">
		<h4 class=\"heading\">Contact Us</h4>
		<div id=\"map\" class=\"googleMap\"></div>
		<div class=\"col_full nobottommargin common-height\">

					<div class=\"col-md-3 dark col-padding ohidden center\" style=\"background-color: #06101a; color:#FFFFFF\">
						<div>
							<h3 class=\"uppercase\" style=\"font-weight: 700; color:#FFFFFF;\">Telephone</h3>
							<p style=\"line-height: 1.1;\">(08) 9034 8654</p>
						</div>
					</div>

					<div class=\"col-md-3 dark col-padding ohidden center\" style=\"background-color: #161d25; color:#FFFFFF\">
						<div>
							<h3 class=\"uppercase\" style=\"font-weight: 700; color:#FFFFFF;\">Fax</h3>
							<p style=\"line-height: 1.1;\">(08) 9034 8654</p>
						</div>
					</div>

					<div class=\"col-md-3 dark col-padding ohidden center\" style=\"background-color: #14181c; color:#FFFFFF\">
						<div>
							<h3 class=\"uppercase\" style=\"font-weight: 700; color:#FFFFFF;\">Email</h3>
							<p style=\"line-height: 1.1;\"><a href=\"mailto:info@theprofessionalrecruiter.com\" style=\"color:#FFFFFF; text-decoration:underline;\">info@theprofessionalrecruiter.com</a></p>
						</div>
					</div>

					<div class=\"col-md-3 dark col-padding ohidden center\" style=\"background-color: #06101a; color:#FFFFFF\">
						<div>
							<h3 class=\"uppercase\" style=\"font-weight: 700; color:#FFFFFF;\">Address</h3>
							<p style=\"line-height: 1.5;\">25 William Street, Perth, WA, 6000. Australia</p>
						</div>
					</div>

					<div class=\"clear\"></div>

				</div>

	</div>
		
	</div>
</section>

<footer>
	<div class=\"toTop\">
		<div class=\"color\"><img src=\"images/footerColor.gif\"></div>
		<div class=\"topButton\" id=\"gotoTop\">TOP</div>
	</div>
	<div class=\"footerMenu\">
		<div class=\"menuRight\">
							<a href=\"index.html\">Home</a>
							<a href=\"about_us.html\">About Us</a>
							<a href=\"our_service.html\">Our Service</a>
							<a href=\"contact.html\">Contact Us</a>
							<span>Copyright @ The Professional Recruiter. All rights reserved.</span>
		</div>
	</div>
</footer>

	</div><!-- #wrapper end -->

	<!-- Go To Top
	============================================= -->

	<!-- External JavaScripts
	============================================= -->
	<script type=\"text/javascript\" src=\"js/jquery.js\"></script>
	<script type=\"text/javascript\" src=\"js/plugins.js\"></script>

	<!-- Footer Scripts
	============================================= -->
	<script type=\"text/javascript\" src=\"js/functions.js\"></script>
<script src=\"https://maps.googleapis.com/maps/api/js?key=AIzaSyAvE9FSI0fEf6900ndOufDIQN1LCY4Dq10&callback=initMap\" async defer></script>

</body>
</html>\n";
