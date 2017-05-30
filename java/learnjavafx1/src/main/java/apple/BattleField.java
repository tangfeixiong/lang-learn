package apple;

import javafx.application.Application;
import javafx.scene.Group;
import javafx.scene.Scene;
import javafx.scene.SnapshotParameters;
import javafx.scene.canvas.Canvas;
import javafx.scene.canvas.GraphicsContext;
import javafx.scene.image.Image;
import javafx.scene.image.ImageView;
import javafx.scene.input.KeyEvent;
import javafx.scene.layout.Pane;
import javafx.scene.layout.Priority;
import javafx.scene.layout.StackPane;
import javafx.scene.layout.HBox;
import javafx.scene.layout.VBox;
import javafx.scene.paint.Color;
import javafx.scene.shape.Rectangle;
import javafx.scene.transform.Rotate;
import javafx.stage.Stage;

import java.io.File;
import java.io.FileInputStream;

public class BattleField extends Application {
	@Override
    public void start(Stage primaryStage) throws Exception {
        Pane pane = new Pane();
        Group group = new Group();

        VBox.setVgrow(group, Priority.NEVER);
        VBox.setVgrow(pane, Priority.NEVER);

        VBox vbox = new VBox(group, pane);

        Rectangle rect1 = new Rectangle(100, 100, 100, 100);
        Rectangle rect2 = new Rectangle(100, 100, 100, 100);
        Rectangle rect3 = new Rectangle(200, 200, 100, 100);
        Rectangle rect4 = new Rectangle(200, 200, 100, 100);
        rect1.setFill(Color.BLUE);
        rect2.setFill(Color.BLUE);
        rect3.setFill(Color.GREEN);
        rect4.setFill(Color.GREEN);
		
		//ClassLoader classloader = Thread.currentThread().getContextClassLoader();
		ClassLoader classLoader = getClass().getClassLoader();
		File file = new File(classLoader.getResource("img/bullet_ammunition_army_shoot-128.png").getFile());
		FileInputStream input = new FileInputStream(file);
        Image image = new Image(input);

        ImageView imageView = new ImageView(image);				
		imageView.setPreserveRatio(true);
		imageView.setFitHeight(32);
        imageView.setFitWidth(32);
		imageView.setRotate(-90);

		SnapshotParameters params = new SnapshotParameters();
		params.setFill(Color.TRANSPARENT);
		Image rotatedImage = imageView.snapshot(params, null);

        Canvas canvas = new Canvas(128, 128);
        GraphicsContext gc = canvas.getGraphicsContext2D();

        drawRotatedImage(gc, image,  -135,   0,   0);
        drawRotatedImage(gc, rotatedImage,  -45,   32,  96);

        StackPane stack = new StackPane();
        stack.setMaxSize(canvas.getWidth(), canvas.getHeight());
        stack.getChildren().add(canvas);

        group.getChildren().addAll(rect1, rect3);
        pane.getChildren().addAll(rect2, rect4, imageView, stack);

        Scene scene = new Scene(vbox, 800, 800);
        scene.addEventHandler(KeyEvent.KEY_PRESSED, e -> {
            double deltaX ;
            switch(e.getCode()) {
                case LEFT:
                    deltaX = -10 ;
                    break ;
                case RIGHT:
                    deltaX = 10 ;
                    break ;
                default:
                    deltaX = 0 ;
            }
            rect3.setX(rect3.getX() + deltaX);
            rect4.setX(rect4.getX() + deltaX);
        });
		
		imageView.setX(imageView.getX() + 400);

        primaryStage.setScene(scene);
        primaryStage.show();
		
		GunScheduler.gunMain(pane, imageView);
    }

    private void rotate(GraphicsContext gc, double angle, double px, double py) {
        Rotate r = new Rotate(angle, px, py);
        gc.setTransform(r.getMxx(), r.getMyx(), r.getMxy(), r.getMyy(), r.getTx(), r.getTy());
    }
	
    private void drawRotatedImage(GraphicsContext gc, Image image, double angle, double tlpx, double tlpy) {
        gc.save(); // saves the current state on stack, including the current transform
        rotate(gc, angle, tlpx + image.getWidth() / 2, tlpy + image.getHeight() / 2);
        gc.drawImage(image, tlpx, tlpy);
        gc.restore(); // back to original state (before rotation)
    }
	
    public static void main(String[] args) {		
        launch(args);
    }
	
} 