import org.junit.Test;

import static org.junit.Assert.*;

public class staffTest {

   @Test(expected=IllegalArgumentException.class)
    public void testExceptionIsThrown(){
       staff tester=new staff();
       tester.new_staff("12@","Prachi","nurse","F",50000);
   }
   @Test
    public void test_staff_id(){
       staff tester=new staff();
       tester.new_staff("12","Prachi","nurse","F",50000);
       assertNotEquals(null,tester.sid);
   }

}