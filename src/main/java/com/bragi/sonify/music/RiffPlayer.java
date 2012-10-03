/*******************************************************************************
 * Copyright (c) 2012 BragiSoft, Inc.
 * This source is subject to the BragiSoft Permissive License.
 * Please see the License.txt file for more information.
 * All other rights reserved.
 * 
 * THIS CODE AND INFORMATION ARE PROVIDED "AS IS" WITHOUT WARRANTY OF ANY 
 * KIND, EITHER EXPRESSED OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE
 * IMPLIED WARRANTIES OF MERCHANTABILITY AND/OR FITNESS FOR A
 * PARTICULAR PURPOSE.
 * 
 * DO NOT ALTER OR REMOVE COPYRIGHT NOTICES OR THIS FILE HEADER.
 *
 * Contributors:
 * Jan-Christoph Klie - Everything but RIFF statics
 * 
 *******************************************************************************/

package com.bragi.sonify.music;

import java.lang.reflect.Field;
import java.util.Random;

import javax.sound.midi.InvalidMidiDataException;
import javax.sound.midi.MidiSystem;
import javax.sound.midi.MidiUnavailableException;
import javax.sound.midi.Receiver;
import javax.sound.midi.ShortMessage;
import javax.sound.midi.Synthesizer;

public class RiffPlayer {
	
	static Random randGen = new Random();
	
	public static void play(Riff riff) throws MidiUnavailableException, InvalidMidiDataException {
		Synthesizer synth = MidiSystem.getSynthesizer();
		synth.open();
		Receiver rcvr = synth.getReceiver();
		ShortMessage msg = new ShortMessage();
		
		for(Note n : riff) {
			msg.setMessage(ShortMessage.NOTE_ON, 0, n.key, 64);
			rcvr.send(msg, -1);
			
			try {
				Thread.sleep((randGen.nextInt(2) + 1) * 400); 
			} catch (Exception e) {
				
			}
			
			msg.setMessage(ShortMessage.NOTE_OFF, 0, n.key, 0);
			rcvr.send(msg, -1);
		}
		
		synth.close();
	}
	
	public static void main(String[] args) {
		try {
			for(int i = 1 ; i <= 94; i++) {
				Field f = Riff.class.getDeclaredField("RIFF"+i);
				Object o = f.get( null );
				play((Riff) o);
			}			
		} catch (MidiUnavailableException | InvalidMidiDataException | NoSuchFieldException | SecurityException | IllegalArgumentException | IllegalAccessException e) {			
			e.printStackTrace();
		}
	}

}
