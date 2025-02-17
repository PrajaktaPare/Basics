import java.awt.event.*;
import java.awt.*;
import javax.swing.*;

public class Swing1 extends JFrame implements ItemListener {
    JLabel font,style,size;
    JComboBox fontcb,sizecb;
    JCheckBox bold,italic;
    JTextField t;
    TextfieldChangesMain()
    {
        p1=new JPanel();
        p2=new JPanel();
        font=new JLabel("Font");
        style=new JLabel("Style");

        fontcb= new JComboBox();
        fontcb.addItem("Arial");
        fontcb.addItem("Sans");
        fontcb.addItem("Monospace");

        bold=new JCheckBox("Bold");
        size=new JLabel("Size");
        italic=new JCheckBox("Italic");

        sizecb=new JComboBox();
        sizecb.addItem("10");
        sizecb.addItem("12");
        sizecb.addItem("16");
        t=new  JTextField(10);

        p1.setLayout(new GridLayout(4,2));
        p1.add(font);
        p1.add(style);
        p1.add(fontcb);
        p1.add(bold);
        p1.add(size);
        p1.add(italic);
        p1.add(sizecb);

        p2.setLayout(new FlowLayout());
        p2.add(t);

        bold.addItemListener(this);
        italic.addItemListener(this);
        fontcb.addItemListener(this);
        sizecb.addItemListener(this);
        
        setLayout(new BorderLayout());
        add(p1,BorderLayout.NORTH);
        add(p2,BorderLayout.CENTER);

        setSize(200,200);
        setVisible(true);

        setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);

    }
    public void  itemsetchanged(ItemEvent ie)
    {
        String f=(String) fontcb.getSelectedItem();
        System.out.println("font = "+f);
        t.setFont(new Font(f,font.Bold,10));
        String no=(String)sizecb.getSelectedItem();
        int num=Integer.pareInt(no);
        if(bold.isSelected())
        {
            t.setFont(new Font(f,Font.BOLD,num));
        }
        if(italic.isSelected())
        {
            t.setFont(new Font(f,Font.ITALIC,num));
        }

    }
    public static void main(String[] args) {
        Swing1 f1= new Swing1();
    }
}
