# Recording command is : playwright codegen https://www.google.com
import re
from playwright.sync_api import Page, expect


def test_example(page: Page) -> None:
    page.goto("https://www.google.com/?zx=1762251379553&no_sw_cr=1")
    expect(page.get_by_role("link", name="Search for Images")).to_be_visible()

    page.get_by_role("combobox", name="Search").click()
    page.get_by_role("combobox", name="Search").fill("playwright")
    page.goto("https://www.google.com/sorry/index?continue=https://www.google.com/search%3Fq%3Dplaywright%26sca_esv%3De6851c063536d12d%26source%3Dhp%26ei%3DctIJaYPGKeft1e8PkOyZ0Ak%26iflsig%3DAOw8s4IAAAAAaQnggivfpF0CPE7LJX3oRNJ2qQhB7UV3%26ved%3D0ahUKEwiDx7n7odiQAxXndvUHHRB2BpoQ4dUDCBA%26uact%3D5%26oq%3Dplaywright%26gs_lp%3DEgdnd3Mtd2l6IgpwbGF5d3JpZ2h0MggQABiABBixAzIIEAAYgAQYsQMyCBAAGIAEGLEDMgUQABiABDIFEAAYgAQyBRAAGIAEMgUQABiABDIFEAAYgAQyBRAAGIAEMgUQABiABEiyRVCqC1j2NnAFeACQAQCYAegDoAGVGKoBCTAuOC41LjAuMbgBA8gBAPgBAZgCE6AC0xioAgrCAgoQABgDGOoCGI8BwgIUEC4YgAQYsQMY0QMYgwEYxwEYigXCAhEQLhiABBixAxjRAxiDARjHAcICCxAAGIAEGLEDGIMBwgIOEC4YgAQYsQMY0QMYxwHCAgsQLhiABBjRAxjHAcICCxAuGIAEGLEDGIMBwgIIEC4YgAQYsQPCAg4QLhiABBixAxiDARiKBcICDhAAGIAEGLEDGIMBGIoFwgIFEC4YgATCAgsQLhiABBjHARivAcICDhAuGIAEGLEDGIMBGNQCwgIREC4YgAQYsQMYgwEY1AIYigXCAgsQABiABBiSAxiKBZgDBfEFgzqbCc96P8qSBwk1LjcuNi4wLjGgB8V7sgcJMC43LjYuMC4xuAfDGMIHBjAuMTUuNMgHLA%26sclient%3Dgws-wiz%26sei%3DgdIJab2yC_rM1e8P5p_m8Ao&q=EgR70JS2GIGlp8gGIjC98JJnJ9M4hrk40o3RWso8gmw9L6rKoilMAEM_O6unhqFX8CJbKzHY0BXPxSZw6IYyAVJaAUM")
    page.locator("iframe[name=\"a-94z1xywjruom\"]").content_frame.get_by_role("checkbox", name="I'm not a robot").click()
    expect(page.get_by_role("row", name="Installation Using npm, yarn")).to_be_visible()

    page.get_by_role("link", name="Playwright: Fast and reliable").click()
