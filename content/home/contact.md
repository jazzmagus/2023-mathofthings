---
# An instance of the Contact widget.
widget: contact

# This file represents a page section.
headless: true

# Order that this section appears on the page.
weight: 130

title: Contact
subtitle:

content:
  # Automatically link email and phone or display as text?
  autolink: true
  
  # Email form provider
  form:
    provider: netlify
    formspree:
      id:
    netlify:
      # Enable CAPTCHA challenge to reduce spam?
      captcha: false

  # Contact details (edit or remove options as required)
  email: diego.fantinelli@gmail.com
  phone: +39 335 5410 558
  address:
    street: via S.ta Croce, 14
    city: Bassano del Grappa
    region: VI
    postcode: '36061'
    country: Italy
    country_code: IT
  coordinates:
    latitude: '45.75488205287305'
    longitude: '11.73475864522695'
  directions: Enter Building 1 and take the stairs to Office 200 on Floor 2
  office_hours:
    - 'Monday 10:00 to 13:00'
    - 'Wednesday 09:00 to 10:00'
 # appointment_url: 'https://calendly.com'
  contact_links:
    - icon: twitter
      icon_pack: fab
      name: DM Me
      link: 'https://twitter.com/jazzmagus'
 #   - icon: video
 #     icon_pack: fas
 #     name: Zoom Me
 #     link: 'https://zoom.com'

design:
  columns: '2'
---
