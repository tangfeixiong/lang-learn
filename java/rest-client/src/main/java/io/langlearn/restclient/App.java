package io.langlearn.restclient;

import com.fasterxml.jackson.annotation.JsonIgnoreProperties;
import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;
import org.springframework.boot.web.client.RestTemplateBuilder;
import org.springframework.web.bind.annotation.*;
import org.springframework.web.client.RestTemplate;
import org.springframework.web.servlet.ModelAndView;

import javax.servlet.http.HttpServletResponse;
import javax.servlet.http.HttpSession;
import java.io.IOException;

@SpringBootApplication
public class App {

	public static void main(String[] args) {
		SpringApplication.run(App.class, args);
	}
}

@RestController
class UserController {

	private final RestTemplate restTemplate;

	UserController(RestTemplateBuilder restTemplateBuilder) {
		this.restTemplate = restTemplateBuilder.build();
	}

    @RequestMapping("/")
    void login(HttpSession session, HttpServletResponse response) throws IOException {
        if (null != session && null != session.getAttribute("user")) {
            response.sendRedirect("/secure/profile");
            return;
        }

        response.setContentType("text/html; charset=UTF-8");
        response.setCharacterEncoding("UTF-8");
        String out = "<html><head>"
                + "<title>sign in</title></head><body>"
                + "<form action=\"/sign-in\" method=\"post\">"
                + "username：<input type=\"text\" name=\"username\" id=\"username\"/><br>"
                + "password：<input type=\"password\" name=\"password\" id=\"password\"/><br>"
                + "<button type=\"submit\" class=\"btn btn-primary\">Submit</button>"
                + "</form></body></html>";
        response.getOutputStream().write(out.getBytes("UTF-8"));
    }

    @RequestMapping(value="/sign-in", method=RequestMethod.POST)
     ModelAndView signIn( Person person, HttpSession session) {
        Person user = this.restTemplate.postForObject("http://127.0.0.1:54321/authenticate", person, Person.class);
        if (0 < user.getId()) {
            user.setUsername(person.getUsername());
            session.setAttribute("user", user);
            return new ModelAndView("redirect:/secure/profile");
        }
        return  null;
    }

    @GetMapping("/secure/profile")
    ModelAndView profile(HttpSession session) {
	    if ( session.isNew() || null == session.getAttribute("user") ) {
            return new ModelAndView("redirect:/");
        }
	    Person user = (Person) session.getAttribute("user");
        return new ModelAndView("/secure/profile", "person", user);
    }

    @GetMapping("/sign-out/{id}")
    String signOut(@PathVariable String id, HttpSession session) {
        if ( null != session.getAttribute("user") ) {
            session.removeAttribute("user");
        }
        System.out.println("User (id=" + id + ") sign out");

        return "redirect:/";
    }
}

@JsonIgnoreProperties
class Person {
	private Integer id;

	private String username;

	private String password;

	private Boolean disabled;

	public Integer getId() {
		return this.id;
	}

	public void setId(int id) {
		this.id = Integer.valueOf(id);
	}

	public String getUsername() {
		return this.username;
	}

	public void setUsername(String username) {
		this.username = username;
	}

	public String getPassword() {
		return this.password;
	}

	public void setPassword(String password) {
		this.password = password;
	}

	public Boolean getDisabled() {
		return this.disabled;
	}

	public void setDisabled(boolean disabled) {
		this.disabled = Boolean.valueOf(disabled);
	}
}


