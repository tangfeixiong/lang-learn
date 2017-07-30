
package examples;

import java.net.*;
import java.io.*;
import java.util.Properties;

import org.apache.commons.io.IOUtils;
 
public class EchoServer {
    public static void main(String[] args) throws IOException {
        int defaultPort = 12345;
        boolean indexFile = false;
		
		Properties props = new Properties(System.getProperties());
	  
	    props.list(System.out);

        if (args.length == 0) {
            System.err.println("Usage: java EchoServer --port=<port number> --indexfile");
            // System.exit(1);
        } else {
	        for ( String item : args) {
	            if (item.matches("--port=\\d{4,5}")) {
				    String port = item.substring("--port=".length(), item.length());
				    int p = Integer.parseInt(port);
					if ( 0 < p && p < 65535 ) {
						defaultPort = p;
					}
			    } else if (item.matches("--indexfile(=(true|false))?")) {
					if (item.toLowerCase() == "--indexfile" || item.replaceAll(" ", "").toLowerCase().endsWith("true")) {
						indexFile = true;
					}
				}
			}
        }

         
        int portNumber = defaultPort; // Integer.parseInt(args[0]);
         
        try (
            ServerSocket serverSocket =
                new ServerSocket(portNumber /*Integer.parseInt(args[0])*/);

            Socket clientSocket = serverSocket.accept();     
            PrintWriter out =
                new PrintWriter(clientSocket.getOutputStream(), true);                   
            BufferedReader in = new BufferedReader(
                new InputStreamReader(clientSocket.getInputStream()));
        ) {
            String inputLine;
            while ((inputLine = in.readLine()) != null) {
               // out.println(inputLine);
				System.out.println(inputLine);
            }
			if (indexFile) {
		        // ClassLoader classLoader = getClass().getClassLoader();
		        // File file = new File(classLoader.getResource("index.html").getFile());
		        // FileInputStream input = new FileInputStream(file);
			    InputStream is = EchoServer.class.getResourceAsStream("/index.html");
			    IOUtils.copy(is, out);
			} else {
				out.println("<html><body><h1>hello world</h1></body></html>");
			}
        } catch (IOException e) {
            System.out.println("Exception caught when trying to listen on port "
                + portNumber + " or listening for a connection");
            System.out.println(e.getMessage());
        }
    }
}