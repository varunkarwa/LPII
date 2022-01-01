import org.junit.Test;

import static org.junit.Assert.*;

public class doctorTest {
    @Test(expected=IllegalArgumentException.class)
    public void testExceptionIsThrown(){
        doctor tester=new doctor();
        tester.new_doctor("12","Prachi","ortho","F","MD",40);
    }

}