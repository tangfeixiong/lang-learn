package apple;

import javafx.scene.Scene;
import javafx.scene.SnapshotParameters;
import javafx.scene.image.Image;
import javafx.scene.image.ImageView;
import javafx.scene.layout.Pane;
import javafx.scene.paint.Color;

import java.util.Date;
import java.util.Timer;
import java.util.TimerTask;

public class GunScheduler implements Runnable {
	private Bullet bullet = new Bullet();
	Pane battlefield;
	int firstFireAfter = 1000;
	int firePeriod = 1 * 3000;

    public void run() {
		GunFireController task = new GunFireController();
		task.img = bullet.topView.getImage();

    	Timer timer = new Timer();
    	timer.schedule(task, firstFireAfter, firePeriod);
		//timer.scheduleAtFixedRate(task, firstFireAfter, firePeriod);

        BulletFlightViewer flight = new BulletFlightViewer();
		flight.bullet = bullet;
		flight.battlefield = battlefield;
		Thread t;
		(t = new Thread( new Runnable() {
			public void run() {
				try {
			        while(true) {			
						synchronized (bullet) {
							System.out.println("Hello from a thread!");
							if ( 0 != bullet.status ) { timer.cancel(); break; }
							bullet.cy += bullet.dy;
							if ( battlefield.getHeight() - 50 < bullet.cy - bullet.y0 ) { bullet.status = 50; break; }
							Thread.sleep(100);
							flight.refresh();
						}
					}
					Thread.sleep(1000);
				} catch (InterruptedException e) {
					
				}
			}
		} )).start();
			
		try {
			t.join(60 * 1000);
			if (t.isAlive()) { t.interrupt(); }
			timer.cancel();
		} catch ( InterruptedException e ) {
			
		}
    }
	
	public synchronized void resetGun(int flag) {
		synchronized (bullet) {
			bullet.status = flag;
		}
	}
	
	public synchronized void resetCombat() {
		this.resetGun(100);
		
	}
	
	public static void gunMain(Pane battlefieldTopView, ImageView bulletTopView) {
		GunScheduler obj = new GunScheduler();
		obj.battlefield = battlefieldTopView;
		obj.bullet.topView = bulletTopView;

		Thread t = new Thread(obj);
		t.start();
	}

    public static void main(String args[]) {
		try {
	        // (new GunScheduler()).start();
			Thread t;
			(t = new Thread(new GunScheduler())).start();
			t.join(5 * 1000);
			if ( t.isAlive() ) {
				t.interrupt();
			}
		} catch ( InterruptedException e ) {
			
		}
    }
}

class Bullet {
	int velocity;
	int acceleration;
	
	int x0 = 0, y0 = 0;
	int dx = 5, dy = 5; 
	int cx = 0, cy = 0;
	
	ImageView topView;
	
	int status = 0;
}

class BulletFlightViewer {
	Bullet bullet;
	Pane battlefield;
	
	public void refresh() {
		System.out.println("flying: (" + bullet.cx + ", " + bullet.cy + ")");
		ImageView view = bullet.topView;
		view.setY(view.getY() + bullet.dy);
	}
}

class GunFireController extends TimerTask {
	Image img;
	Bullet bullet;
	
	@Override
	public void run() {
    	System.out.println("Firing ~" + new Date());
		bullet = new Bullet();
		bullet.topView = new ImageView(img);
	}
}