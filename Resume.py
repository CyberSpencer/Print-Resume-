# Print(Resume).py
# Author: Spencer Thomson
# Date: 10/23/2023
# Description: A Python script to create my own interactive resume.
#              The script offers a menu-driven interface for the user to view various
#              sections of my resume like; contact info, objective, certifications,
#              skills, work experience, and education. Each section is further
#              organized for easy readability and navigation.


class Resume:
    def __init__(self):
        self.contact_info = (
            "Spencer Thomson\n"
            "(719) 238 -2519\n"
            "Spencertsales@gmail.com\n"
            "Github.com/CyberSpencer\n"
            "Linkedin.com/in/spencer-thomson-43365b11a/\n"
        )
        self.objective = (
            "Seeking a remote cybersecurity role to leverage my recently acquired "
            "Google Cybersecurity Certificate and my diverse background in risk "
            "management, data handling, and systems development, while also pursuing "
            "further education, mentorship, and skill development."
        )
        self.certifications = (
            "Google Cybersecurity Certificate: Completed 10/23\n"
            "  - Familiar with laws and regulations such as: GDPR, HIPPA, PCI DSS\n"
            "  - Experience using: SPLUNK, Chronicle, Wireshark, TCPDump, Linux, Port Filtering\n"
            "  - Familiar with: TCP/IP, Hashes, IPv4+IPv6, WPA2+WPA3, MFA, NIST-CSF\n"
            "  - Course Grade = Average of 93.86%\n"
            "IBM Windows Defender & Firewall for Beginners: Completed 10/23\n"
            "Wireshark for Beginners: Capture Packets: Completed 10/23\n"
            "Analyze Network Traffic with TCPDump: Completed 10/23\n"
            "CompTIA Security+: Planned Examination: 12/23"
        )
        self.skills = (
            "Programming Languages: Python, SQL, Bash/Zsh, Excel VBA (Entry level skills)\n"
            "Data Analysis & Visualization: Proficient in creating and interpreting large data sets, "
            "while maintaining the Confidentiality, Integrity and Availability of that data.\n"
            "Web Development: WordPress, 10web, basic understanding of CSS\n"
            "Projects: Please Visit my GitHub to review my Cyber Security Projects ;)"
        )
        self.education_certifications = {
            "The Vanguard School, Colorado Springs, CO": {
                "Highlights": [
                    "Graduated December 2014 (a semester early) with a 3.8 GPA.",
                    "Achieved a 32 ACT super score, PSAT National Merit Scholar in Mathematics.",
                    "Founded the Debate Club, participated for 3 years, and achieved state finals."
                ]
            },
            "Snow Trainer Class of 2016, Queenstown, New Zealand": {},
            "Wilderness First Responder (WFR)": {
                "Certifications": [
                    "CPR certifications for youth to adults."
                ]
            },
            "Avalanche Certifications": {
                "Details": [
                    "Avalanche 1 & Avalanche Rescue Certifications (95% complete w/ my Avalanche Pro 1)"
                ]
            },
            "Other Certifications": {
                "Details": [
                    "AMGA SPI, SPRAT High Angle Rescue Tech and Bonsai Level 2 Zipline Practitioner."
                ]
            }
        }

    def display_work_experience(self):
         while True:
            print("\nWork Experience Menu:")
            print("a. Awesome Accounting, Colorado Springs, CO")
            print("b. Black Diamond Equipment, Big Sky, MT")
            print("c. CarScoutsUSA LLC, Los Angles, California")
            print("d. Colorado Climbing Company / Montana Alpine Guides")
            print("e. Monarch Mountain, Salida, CO")
            print("f. Royal Gorge Bridge Park, Canyon City, CO")
            print("g. Colorado Mountain College, Steamboat Springs, CO")
            print("h. Pikes Peak Acura, Colorado Springs, CO")
            print("i. Vail Resorts, Keystone, Colorado")
            print("j. Crested Butte Mountain Resort, Crested Butte, Colorado")
            print("99. Back to Main Menu")

            choice = input("Enter your choice (a-j or 99 to exit): ")

            if choice == 'a':
                print("\nAwesome Accounting, Colorado Springs, CO: 1/23 to Current\n"
                      "  - Audit invoices in Quickbooks ensuring availability, confidentiality & integrity of data.\n"
                      "  - Convey complex data insights with visual data representation to stakeholders\n"
                      "  - Manage website development projects on WordPress and 10web.\n")
            elif choice == 'b':
                print("\nBlack Diamond Equipment, Big Sky, MT: 9/20 to 5/21\n"
                      "  - Educated staff on the proper use of safety equipment and a risk management mindset.\n"
                      "  - Compiled and communicated sensitive data on store performance through nightly emails.\n"
                      "  - Designed a spreadsheet system to track store KPIs, presenting visual data representations.\n")
            elif choice == 'c':
                print("\nCarScoutsUSA LLC, Los Angles, California: 4/14 to 12/14\n"
                      "  - Co-founded an LLC at 16, ensuring compliance with automotive wholesaler regulations.\n"
                      "  - Developed a car appraisal system using Excel VBA, screen scraping code and a proprietary algorithm.\n"
                      "  - Created and managed a confidential data set of over 100k rows and 15 columns in .xls\n")
            elif choice == 'd':
                print("\nColorado Climbing Company / Montana Alpine Guides: 7/20 to 8/22\n"
                      "  - Guide Rock climbing, mountaineering and Split-boarding across the western US\n"
                      "  - Experience with Risk Management in high stress / high stakes environments\n"
                      "  - Communication & assessment of risks & vulnerabilities in individual and team settings\n")
            elif choice == 'e':
                print("\nMonarch Mountain, Salida, CO: 11/19 to 4/20 & 11/21 to 3/22\n"
                      "  - Taught Snowboarding and Skiing to all ages and abilities\n"
                      "  - Taught Split-boarding and basic backcountry risk mitigation to fellow instructors\n")
            elif choice == 'f':
                print("\nRoyal Gorge Bridge Park, Canyon City, Co: 4/19 to 7/19\n"
                      "  - Trained staff on rope rescue procedure / risk management mindset\n"
                      "  - Helped build the Via Ferrata Course / filled out hundreds of legal documents/inspections\n"
                      "  - Performed safety inspections on equipment, including the required paperwork\n")
            elif choice == 'g':
                print("\nColorado Mountain College, Steamboat Springs, Co: 1/18 to 8/18\n"
                      "  - Constructed and maintained campus Ski / Snowboard park (Including documentation)\n")
            elif choice == 'h':
                print("\nPikes Peak Acura, Colorado Springs, Co: 6/17 to 9/17\n"
                      "  - Marketing and Sales of Cars\n")
            elif choice == 'i':
                print("\nVail Resorts, Keystone, Colorado: 2/17 to 6/17\n"
                      "  - Snowboard and Ski Instructor for kids to adults of all ability levels\n")
            elif choice == 'j':
                print("\nCrested Butte Mountain Resort, Crested Butte, Colorado: 11/15 to 2/17\n"
                      "  - Snowboard and ski Instructor for kids to adults of all ability levels\n")

            elif choice == '99':
                print("Returning to main menu...")
                break
            else:
                print("Invalid choice. Please try again.")


    def display_education(self):
        while True:
            print("\nEducation & Non-Cybersecurity Certifications Menu:")
            for school, details in self.education_certifications.items():
                print(f"{school}")
                for detail, value in details.items():
                    print(f"  {detail}: {', '.join(value)}")
            print("99. Back to Main Menu")

            choice = input("Enter 99 to go back to the main menu: ")

            if choice == '99':
                print("Returning to main menu...")
                break
            else:
                print("Invalid choice. Please try again.")

def display_menu():
    print("\nInteractive Resume - Spencer Thomson")
    print("1. View Contact Info")
    print("2. View Objective")
    print("3. View Certifications & Skills")
    print("4. View Work Experience")
    print("5. View Education & Non-Cybersecurity Certifications")
    print("9. Exit")

def interactive_resume():
    spencer_resume = Resume()

    while True:
        display_menu()  # Call the function to display the main menu
        
        choice = input("Enter your choice (1-9): ")

        if choice == '1':
            print(f"\nContact Info:\n{spencer_resume.contact_info}\n")
        elif choice == '2':
            print(f"\nObjective:\n{spencer_resume.objective}\n")
        elif choice == '3':
            print(f"\nCertifications & Skills:\n{spencer_resume.certifications}\n{spencer_resume.skills}\n")
        elif choice == '4':
            spencer_resume.display_work_experience()  # Call the method to display the work experience submenu
        elif choice == '5':
            spencer_resume.display_education()  # Call the method to display the education submenu
        elif choice == '9':
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    interactive_resume()
