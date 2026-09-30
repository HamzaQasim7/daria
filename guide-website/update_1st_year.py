import re

with open('1st-year.html', 'r', encoding='utf-8') as f:
    content = f.read()

new_books = """        <!-- Books -->
        <section id="books" class="pdf-section">
            <div class="pdf-header">13 / Books</div>
            <h2 class="pdf-title">SIX BOOKS I WOULD KEEP NEAR MY DESK.</h2>
            <div class="pdf-content">
                <p>You do not need to finish them before semester starts. Read slowly and return when a project gives you a reason.</p>

                <div class="pdf-list">
                    <div class="pdf-list-item">
                        <div class="pdf-list-number">01</div>
                        <div class="pdf-list-content">
                            <h3>EXPERIENCING ARCHITECTURE</h3>
                            <p>Steen Eiler Rasmussen<br><em>proportion / rhythm / perception</em></p>
                        </div>
                    </div>
                    <div class="pdf-list-item">
                        <div class="pdf-list-number">02</div>
                        <div class="pdf-list-content">
                            <h3>LESSONS FOR STUDENTS IN ARCHITECTURE</h3>
                            <p>Herman Hertzberger<br><em>space / use / project thinking</em></p>
                        </div>
                    </div>
                    <div class="pdf-list-item">
                        <div class="pdf-list-number">03</div>
                        <div class="pdf-list-content">
                            <h3>THE EYES OF THE SKIN</h3>
                            <p>Juhani Pallasmaa<br><em>architecture beyond the image</em></p>
                        </div>
                    </div>
                    <div class="pdf-list-item">
                        <div class="pdf-list-number">04</div>
                        <div class="pdf-list-content">
                            <h3>ATMOSPHERES</h3>
                            <p>Peter Zumthor<br><em>material / sound / temperature / mood</em></p>
                        </div>
                    </div>
                    <div class="pdf-list-item">
                        <div class="pdf-list-number">05</div>
                        <div class="pdf-list-content">
                            <h3>A PATTERN LANGUAGE</h3>
                            <p>Christopher Alexander et al.<br><em>spatial questions / everyday life</em></p>
                        </div>
                    </div>
                    <div class="pdf-list-item">
                        <div class="pdf-list-number">06</div>
                        <div class="pdf-list-content">
                            <h3>CARLO SCARPA: ARCHITECTURE IN DETAILS</h3>
                            <p>various studies<br><em>junctions / craft / physical precision</em></p>
                        </div>
                    </div>
                </div>
            </div>

            <div class="dark-callout" style="background-color: var(--color-brand-900);">
                DO NOT READ ARCHITECTURE TO SOUND LIKE AN ARCHITECT.<br>
                <span style="font-size: 1rem; text-transform: none; font-weight: 400; letter-spacing: normal; color: var(--color-secondary-100);">Read it because your next project needs a better question.</span>
            </div>
        </section>

        <!-- Revit -->
        <section id="revit" class="pdf-section">
            <div class="pdf-header">04 / Revit</div>
            <h2 class="pdf-title">LEARN REVIT AS A DESIGN TOOL.</h2>
            <div class="pdf-content">
                <p>I would learn plan and section together from the beginning. The model is useful only if it helps you make architectural decisions.</p>
                <img src="/pdf_images/page_7_img_1.jpeg" alt="Revit Plan" class="feature-image" style="margin: 2rem 0;">
                <div class="pdf-list">
                    <div class="pdf-list-item"><div class="pdf-list-number">01</div><div class="pdf-list-content"><h3>levels + grids</h3></div></div>
                    <div class="pdf-list-item"><div class="pdf-list-number">02</div><div class="pdf-list-content"><h3>walls + openings</h3></div></div>
                    <div class="pdf-list-item"><div class="pdf-list-number">03</div><div class="pdf-list-content"><h3>stairs</h3></div></div>
                    <div class="pdf-list-item"><div class="pdf-list-number">04</div><div class="pdf-list-content"><h3>rooms + furniture</h3></div></div>
                    <div class="pdf-list-item"><div class="pdf-list-number">05</div><div class="pdf-list-content"><h3>plans + sections</h3></div></div>
                    <div class="pdf-list-item"><div class="pdf-list-number">06</div><div class="pdf-list-content"><h3>simple sheets</h3></div></div>
                </div>
                <div class="dark-callout">
                    DO NOT OVERMODEL<br>
                    <span style="font-size: 1rem; font-weight: 400; text-transform: none;">Model what you need to make the next decision. First year is not a BIM competition.</span>
                </div>
            </div>
        </section>

        <!-- Visoid -->
        <section id="visoid" class="pdf-section">
            <div class="pdf-header">05 / Visoid</div>
            <h2 class="pdf-title">VISUALISE AFTER YOU HAVE A POINT OF VIEW.</h2>
            <div class="pdf-content">
                <p>A beautiful image should clarify architecture, not convince you to stop questioning it.</p>
                <img src="/pdf_images/page_8_img_1.jpeg" alt="Visoid Render" class="feature-image" style="margin: 2rem 0;">
                <ol style="list-style: decimal; font-family: var(--font-display); font-size: 1.5rem; padding-left: 2rem;">
                    <li><span style="font-family: var(--font-sans); font-size: 1rem;">Decide what the view needs to explain.</span></li>
                    <li><span style="font-family: var(--font-sans); font-size: 1rem;">Export a clear architectural base from Revit.</span></li>
                    <li><span style="font-family: var(--font-sans); font-size: 1rem;">Use references intentionally: material, light, mood.</span></li>
                    <li><span style="font-family: var(--font-sans); font-size: 1rem;">Explore visual directions in Visoid.</span></li>
                    <li><span style="font-family: var(--font-sans); font-size: 1rem;">Choose and refine instead of generating endlessly.</span></li>
                    <li><span style="font-family: var(--font-sans); font-size: 1rem;">Finish only what matters in Photoshop.</span></li>
                </ol>
            </div>
        </section>

        <!-- Photoshop -->
        <section id="photoshop" class="pdf-section">
            <div class="pdf-header">06 / Photoshop</div>
            <h2 class="pdf-title">PHOTOSHOP IS NOT JUST FOR MAKING IT PRETTY.</h2>
            <div class="pdf-content">
                <img src="/pdf_images/page_9_img_1.jpeg" alt="Photoshop Render" class="feature-image" style="margin: 2rem 0;">
                <div class="pdf-list">
                    <div class="pdf-list-item"><div class="pdf-list-content"><h3>01 HIERARCHY</h3><p>Control what the eye sees first.</p></div></div>
                    <div class="pdf-list-item"><div class="pdf-list-content"><h3>02 ATMOSPHERE</h3><p>Light, people and texture should support the spatial idea.</p></div></div>
                    <div class="pdf-list-item"><div class="pdf-list-content"><h3>03 COLLAGE</h3><p>A fast collage can test an idea before a polished render is worth making.</p></div></div>
                    <div class="pdf-list-item"><div class="pdf-list-content"><h3>04 DIAGRAMS</h3><p>Simple graphics are often stronger than over-designed ones.</p></div></div>
                    <div class="pdf-list-item"><div class="pdf-list-content"><h3>05 FINAL CONTROL</h3><p>Colour, contrast and consistency before layout.</p></div></div>
                </div>
            </div>
        </section>

        <!-- InDesign -->
        <section id="indesign" class="pdf-section">
            <div class="pdf-header">07 / InDesign</div>
            <h2 class="pdf-title">YOUR PRESENTATION IS PART OF THE PROJECT.</h2>
            <div class="pdf-content">
                <p>InDesign is where I would learn to edit: hierarchy, sequence, white space and what deserves to be large.</p>
                <img src="/pdf_images/page_10_img_1.jpeg" alt="InDesign Layout" class="feature-image" style="margin: 2rem 0;">
                <div class="pdf-list">
                    <div class="pdf-list-item"><div class="pdf-list-content"><h3>01 ONE HERO</h3><p>Decide what should be understood first.</p></div></div>
                    <div class="pdf-list-item"><div class="pdf-list-content"><h3>02 ONE GRID</h3><p>Use alignment instead of decorating empty space.</p></div></div>
                    <div class="pdf-list-item"><div class="pdf-list-content"><h3>03 FEWER FONT SIZES</h3><p>Typography should organise, not perform.</p></div></div>
                    <div class="pdf-list-item"><div class="pdf-list-content"><h3>04 WHITE SPACE</h3><p>Do not fill every centimetre.</p></div></div>
                    <div class="pdf-list-item"><div class="pdf-list-content"><h3>05 PRINT TEST</h3><p>Always.</p></div></div>
                </div>
            </div>
        </section>

        <!-- Case Study: Concept -->
        <section id="case-study-concept" class="pdf-section">
            <div class="pdf-header">11 / Case Study</div>
            <h2 class="pdf-title">ONE PROJECT. ONE IDEA. MANY SCALES.</h2>
            <div class="pdf-content">
                <p>I want to show this as a project workflow, not as a collection of final images.</p>
                <h3>01 / EXPERIENCE FIRST</h3>
                <p>The project begins with the relationship between landscape, retreat and a slower sequence of arrival. Before details, the project needs a clear spatial intention.</p>
                <img src="/pdf_images/page_11_img_1.jpeg" alt="Concept" class="feature-image" style="margin: 2rem 0;">
                <h4>WHAT TO NOTICE</h4>
                <ol style="list-style: decimal; padding-left: 2rem;">
                    <li>the building sits low in the landscape</li>
                    <li>the circular form organises movement</li>
                    <li>architecture and landscape are read together before the room</li>
                </ol>
            </div>
        </section>

        <!-- Case Study: Plan + Section -->
        <section id="case-study-plan" class="pdf-section">
            <div class="pdf-header">12 / Case Study</div>
            <h2 class="pdf-title">PLAN + SECTION HAVE DIFFERENT JOBS.</h2>
            <div class="pdf-content">
                <img src="/pdf_images/page_12_img_1.jpeg" alt="Section" class="feature-image" style="margin: 2rem 0;">
                <img src="/pdf_images/page_12_img_2.jpeg" alt="Plan" class="feature-image" style="margin: 2rem 0;">
                <p><strong>PLAN:</strong> Organisation, sequence, programme, circulation and the geometry of the central space.</p>
                <p><strong>SECTION:</strong> Level changes, ground, light, structure and the relationship between interior and landscape.</p>
                <div class="dark-callout">
                    FIRST-YEAR EXERCISE<br>
                    <span style="font-size: 1rem; font-weight: 400; text-transform: none;">Take one project you admire. Cover the images. Try to explain the idea using only one plan and one section.</span>
                </div>
            </div>
        </section>

        <!-- Case Study: Detail -->
        <section id="case-study-detail" class="pdf-section">
            <div class="pdf-header">13 / Case Study</div>
            <h2 class="pdf-title">THE PROJECT GETS MORE PRECISE.</h2>
            <div class="pdf-content">
                <p>The closer the scale, the more specific the decisions become.</p>
                <img src="/pdf_images/page_13_img_1.jpeg" alt="Room" class="feature-image" style="margin: 2rem 0;">
                <img src="/pdf_images/page_13_img_2.jpeg" alt="Detail" class="feature-image" style="margin: 2rem 0;">
                <h3>WHAT CHANGES?</h3>
                <p>At room and detail scale, proportion becomes material, junction, build-up, drainage and the exact way someone touches the architecture.</p>
            </div>
        </section>

        <!-- Where I would learn -->
        <section id="where-to-learn" class="pdf-section">
            <div class="pdf-header">14 / Learning</div>
            <h2 class="pdf-title">COURSES I WOULD ACTUALLY LOOK AT.</h2>
            <div class="pdf-content">
                <p>My rule: learn one thing, use it immediately in your current project, then learn the next thing.</p>
                <div class="pdf-list">
                    <div class="pdf-list-item"><div class="pdf-list-content"><h3>OT 0 DO 10 / @ot0do10</h3><p>BEST FOR: structured architecture learning. OPEN RESOURCE</p></div></div>
                    <div class="pdf-list-item"><div class="pdf-list-content"><h3>SOFT CULTURE</h3><p>BEST FOR: software through architecture. OPEN RESOURCE</p></div></div>
                    <div class="pdf-list-item"><div class="pdf-list-content"><h3>GROMARCH</h3><p>BEST FOR: visuals + graphics + workflow. OPEN RESOURCE</p></div></div>
                </div>
                <div class="dark-callout">
                    DO NOT SAVE 200 TUTORIALS.<br>
                    <span style="font-size: 1rem; font-weight: 400; text-transform: none;">Finish one focused course and use it on a real project.</span>
                </div>
            </div>
        </section>

        <!-- Project Start -->
        <section id="project-start" class="pdf-section">
            <div class="pdf-header">15 / Project Start</div>
            <h2 class="pdf-title">DO NOT START WITH PINTEREST.</h2>
            <div class="pdf-content">
                <p>Start by understanding the problem. Inspiration becomes useful only after you know what you are looking for.</p>
                <div class="pdf-list">
                    <div class="pdf-list-item"><div class="pdf-list-content"><h3>01 WHAT IS THE SITE DOING?</h3><p>Light, access, slope, neighbours, noise, views, existing structure.</p></div></div>
                    <div class="pdf-list-item"><div class="pdf-list-content"><h3>02 WHO IS THIS FOR?</h3><p>Imagine real routines, not an abstract 'user'.</p></div></div>
                    <div class="pdf-list-item"><div class="pdf-list-content"><h3>03 WHAT IS THE ONE IDEA?</h3><p>If you cannot explain it in one sentence, it is probably not clear enough yet.</p></div></div>
                    <div class="pdf-list-item"><div class="pdf-list-content"><h3>04 WHAT MUST THE PLAN SOLVE?</h3><p>Circulation, privacy, daylight, dimensions, thresholds, storage.</p></div></div>
                    <div class="pdf-list-item"><div class="pdf-list-content"><h3>05 WHAT MUST THE SECTION SOLVE?</h3><p>Height, light, levels, structure, relation to landscape.</p></div></div>
                </div>
                <p><strong>THEN LOOK FOR REFERENCES THAT ANSWER THOSE QUESTIONS.</strong></p>
            </div>
        </section>

        <!-- References Dissect -->
        <section id="references-dissect" class="pdf-section">
            <div class="pdf-header">17 / References</div>
            <h2 class="pdf-title">DO NOT SAVE A BUILDING. DISSECT IT.</h2>
            <div class="pdf-content">
                <ol style="list-style: decimal; padding-left: 2rem;">
                    <li>What is the plan doing that mine is not?</li>
                    <li>Where is the main circulation sequence?</li>
                    <li>How does the section bring in light?</li>
                    <li>What is structural and what only looks structural?</li>
                    <li>Where do materials change - and why there?</li>
                    <li>How does the building meet the ground?</li>
                    <li>What happens at the door, window, corner and threshold?</li>
                    <li>What would still be good if the render was ugly?</li>
                </ol>
                <div class="dark-callout">A REFERENCE IS A QUESTION YOU CAN LEARN FROM.</div>
            </div>
        </section>

        <!-- Buildings to study -->
        <section id="buildings" class="pdf-section">
            <div class="pdf-header">18 / Buildings</div>
            <h2 class="pdf-title">SIX PROJECTS. SIX DIFFERENT LESSONS.</h2>
            <div class="pdf-content">
                <div class="pdf-list">
                    <div class="pdf-list-item"><div class="pdf-list-content"><h3>ALVARO SIZA: LECA SWIMMING POOLS</h3><p>STUDY: building + landscape</p></div></div>
                    <div class="pdf-list-item"><div class="pdf-list-content"><h3>TADAO ANDO: CHURCH OF THE LIGHT</h3><p>STUDY: light as architecture</p></div></div>
                    <div class="pdf-list-item"><div class="pdf-list-content"><h3>CARLO SCARPA: CASTELVECCHIO</h3><p>STUDY: junctions + stairs</p></div></div>
                    <div class="pdf-list-item"><div class="pdf-list-content"><h3>MIES VAN DER ROHE: NEUE NATIONALGALERIE</h3><p>STUDY: structure + proportion</p></div></div>
                    <div class="pdf-list-item"><div class="pdf-list-content"><h3>PETER ZUMTHOR: THERME VALS</h3><p>STUDY: material + sequence</p></div></div>
                    <div class="pdf-list-item"><div class="pdf-list-content"><h3>LACATON & VASSAL: GRAND PARC BORDEAUX</h3><p>STUDY: generosity + reuse</p></div></div>
                </div>
            </div>
        </section>

        <!-- Crits -->
        <section id="crits" class="pdf-section">
            <div class="pdf-header">20 / Crits</div>
            <h2 class="pdf-title">ARRIVE WITH A QUESTION, NOT A PANIC.</h2>
            <div class="pdf-content">
                <h3>FOR A CRIT</h3>
                <div class="pdf-list">
                    <div class="pdf-list-item"><div class="pdf-list-content"><h3>01 START WITH ONE SENTENCE</h3><p>What is the project trying to do?</p></div></div>
                    <div class="pdf-list-item"><div class="pdf-list-content"><h3>02 SHOW THE RIGHT DRAWING FIRST</h3><p>The clearest drawing, not necessarily the prettiest.</p></div></div>
                    <div class="pdf-list-item"><div class="pdf-list-content"><h3>03 ASK ONE SPECIFIC QUESTION</h3><p>Make it possible to give you useful feedback.</p></div></div>
                    <div class="pdf-list-item"><div class="pdf-list-content"><h3>04 WRITE FEEDBACK DOWN</h3><p>You will not remember everything afterwards.</p></div></div>
                    <div class="pdf-list-item"><div class="pdf-list-content"><h3>05 DO NOT CHANGE EVERYTHING</h3><p>Separate useful criticism from personal preference.</p></div></div>
                </div>
            </div>
        </section>

        <!-- Interactive Workbook -->
        <section id="workbook" class="pdf-section">
            <div class="pdf-header">21 / Workbook</div>
            <h2 class="pdf-title">BUILD YOUR FIRST PROJECT SYSTEM.</h2>
            <div class="pdf-content">
                <ol style="list-style: decimal; padding-left: 2rem;">
                    <li><strong>THE BRIEF:</strong> What is actually being asked?</li>
                    <li><strong>THE QUESTION:</strong> What is the one spatial problem I am solving?</li>
                    <li><strong>THE SITE:</strong> What must I respond to?</li>
                    <li><strong>THE USER:</strong> What everyday routine matters?</li>
                    <li><strong>REFERENCES:</strong> What do I need to learn from them?</li>
                    <li><strong>NEXT DECISION:</strong> What exactly do I need to resolve next?</li>
                </ol>
            </div>
        </section>

        <!-- Checklist -->
        <section id="checklist" class="pdf-section">
            <div class="pdf-header">22 / Checklist</div>
            <h2 class="pdf-title">FIRST YEAR STARTER CHECKLIST.</h2>
            <div class="pdf-content">
                <ul style="list-style: square; padding-left: 2rem; font-size: 1.125rem; line-height: 1.8;">
                    <li>Install Revit and learn the basic interface.</li>
                    <li>Create one tiny practice model - not a full project.</li>
                    <li>Learn Photoshop selections, masks, layers and adjustment tools.</li>
                    <li>Learn pages, grids and paragraph styles in InDesign.</li>
                    <li>Bookmark 3-4 architecture reference sources you trust.</li>
                    <li>Study one building properly: plan + section + detail + photos.</li>
                    <li>Create a clean folder and file-naming system.</li>
                    <li>Set up automatic backups.</li>
                    <li><strong>Remember: you are allowed to be a beginner.</strong></li>
                </ul>
            </div>
        </section>
"""

footer = """
    <!-- Footer -->
    <footer class="site-footer">
        <div class="footer-top">
            <div class="footer-logo">DARIA ZYGINA</div>
            <div class="footer-socials">
                <a href="https://www.instagram.com/dashazygina?utm_source=ig_web_button_share_sheet&stkn=ZDNlZDc0MzIxNw==" target="_blank" rel="noopener noreferrer">Instagram</a>
                <a href="https://www.linkedin.com/in/daria-zygina-219661233/" target="_blank" rel="noopener noreferrer">LinkedIn</a>
            </div>
        </div>
        <div class="footer-bottom">
            <p>&copy; 2026 Daria Zygina. All rights reserved.</p>
            <p>Designed with purpose.</p>
        </div>
    </footer>
"""

start_idx = content.find('<!-- Books -->')

new_content = content[:start_idx] + new_books + '\n    </main>\n' + footer + '\n    <script type="module" src="/src/main.js"></script>\n  </body>\n</html>'

with open('1st-year.html', 'w', encoding='utf-8') as f:
    f.write(new_content)
print('Success!')
