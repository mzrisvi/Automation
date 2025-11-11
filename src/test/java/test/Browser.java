package test;

import java.io.File;
import java.io.IOException;
import java.time.Duration;

import org.apache.commons.io.FileUtils;
import org.openqa.selenium.By;
import org.openqa.selenium.JavascriptExecutor;
import org.openqa.selenium.OutputType;
import org.openqa.selenium.TakesScreenshot;
import org.openqa.selenium.WebDriver;
import org.openqa.selenium.WebElement;
import org.openqa.selenium.WindowType;
import org.openqa.selenium.chrome.ChromeDriver;

public class Browser {

    public static void main(String[] args) throws InterruptedException, IOException {
        WebDriver driver = new ChromeDriver();

        driver.manage().timeouts().implicitlyWait(Duration.ofSeconds(20));
        driver.manage().timeouts().scriptTimeout(Duration.ofMinutes(2));
        driver.manage().timeouts().pageLoadTimeout(Duration.ofSeconds(10));

        driver.get("https://google.com");
        String original = driver.getWindowHandle();
        //driver.navigate().to("https://automationstepbystep.com/");

        System.out.println(driver.getCurrentUrl());
        System.out.println(driver.getTitle());

        driver.manage().window().minimize();
        driver.manage().window().maximize();

        // Screenshots taking
        File scrFile = ((TakesScreenshot) driver).getScreenshotAs(OutputType.FILE);
        FileUtils.copyFile(scrFile, new File("./image1.png"));

        WebElement element = driver.findElement(By.cssSelector(".lnXdpd"));
        File scrFile1 = element.getScreenshotAs(OutputType.FILE);
        FileUtils.copyFile(scrFile1, new File("./image2.png"));

        // Create JavascriptExecutor interface object by Type casting
        JavascriptExecutor js = (JavascriptExecutor) driver;

        // Get return value from script
        WebElement button = driver.findElement(By.name("btnI"));
        String text = (String) js.executeScript("return arguments[0].innerText", button);

        // JavaScript to click element
        js.executeScript("arguments[0].click();", button);

        // Execute JS directly
        js.executeScript("console.log('Hello World')");

        driver.navigate().back();
        Thread.sleep(2000);
        driver.navigate().forward();
        driver.navigate().refresh();

        driver.switchTo().window(original);
        driver.switchTo().newWindow(WindowType.WINDOW);
        driver.switchTo().newWindow(WindowType.TAB);

        // driver.close();
    }

}
